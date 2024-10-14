import pandas as pd
import re
import os
import html
import string
from collections import Counter
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Replace with the actual path to your TSV file
data_file = os.path.join(proj_path, "clues/all-clues/all_data_cleaned.tsv")

# Read the TSV file into a DataFrame
df = pd.read_csv(data_file, sep='\t', encoding='utf-8', dtype={'round': 'Int64', 'daily_double_value': 'Int64'})

# -----------------------------
# Step 3: Data Validation Checks
# -----------------------------

# 3.1 Validate 'round' Column
valid_rounds = [1, 2, 3]
invalid_rounds = df[~df['round'].isin(valid_rounds) | df['round'].isna()]

if not invalid_rounds.empty:
    print("Rows with invalid 'round' values:")
    print(invalid_rounds[['round', 'category', 'question', 'answer']])
else:
    print("All 'round' values are valid.")

# 3.2 Validate 'daily_double_value' Column
valid_dd_values = [0, 1]
invalid_dd = df[~df['daily_double_value'].isin(valid_dd_values) | df['daily_double_value'].isna()]

if not invalid_dd.empty:
    print("\nRows with invalid 'daily_double_value' values:")
    print(invalid_dd[['daily_double_value', 'category', 'question', 'answer']])
else:
    print("All 'daily_double_value' values are valid.")

# 3.3 Check for Missing 'category', 'answer', 'question'
missing_fields = df[df[['category', 'answer', 'question']].isnull().any(axis=1)]

if not missing_fields.empty:
    print("\nRows with missing 'category', 'answer', or 'question':")
    print(missing_fields[['category', 'answer', 'question']])
else:
    print("No missing 'category', 'answer', or 'question' fields.")

# -----------------------------
# Step 4: Weird Characters Check
# -----------------------------

def find_weird_characters(text):
    if pd.isnull(text):
        return set()
    # Define acceptable characters (printable ASCII)
    acceptable_chars = set(string.printable)
    # Find characters not in acceptable_chars
    weird_chars = set(text) - acceptable_chars
    return weird_chars

text_columns = ['category', 'question', 'answer', 'notes', 'comments']
weird_characters = set()

for col in text_columns:
    for text in df[col].dropna():
        weird_chars_in_text = find_weird_characters(text)
        weird_characters.update(weird_chars_in_text)

if weird_characters:
    print("\nWeird characters found in text columns:")
    print(weird_characters)
else:
    print("No weird characters found in text columns.")

# -----------------------------
# Step 5: Backslash Analysis
# -----------------------------

total_backslashes = 0
backslash_followed_by_single_quote = 0
backslash_followed_by_double_quote = 0
backslash_followed_by_other = 0
lone_backslashes = []

for idx, row in df.iterrows():
    for col in text_columns:
        text = str(row[col])
        backslashes_in_text = re.findall(r'\\', text)
        total_backslashes += len(backslashes_in_text)
        for match in re.finditer(r'\\.', text):
            next_char = match.group()[1]  # Character after backslash
            if next_char == "'":
                backslash_followed_by_single_quote += 1
            elif next_char == '"':
                backslash_followed_by_double_quote += 1
            else:
                backslash_followed_by_other += 1
                lone_backslashes.append({'index': idx, 'column': col, 'context': text[max(0, match.start()-10):match.end()+10]})

# Calculate Percentages
total_backslash_sequences = backslash_followed_by_single_quote + backslash_followed_by_double_quote + backslash_followed_by_other

if total_backslash_sequences > 0:
    perc_single_quote = (backslash_followed_by_single_quote / total_backslash_sequences) * 100
    perc_double_quote = (backslash_followed_by_double_quote / total_backslash_sequences) * 100
    perc_other = (backslash_followed_by_other / total_backslash_sequences) * 100

    print(f"\nBackslash followed by single quote: {backslash_followed_by_single_quote} times ({perc_single_quote:.2f}%)")
    print(f"Backslash followed by double quote: {backslash_followed_by_double_quote} times ({perc_double_quote:.2f}%)")
    print(f"Backslash followed by other characters: {backslash_followed_by_other} times ({perc_other:.2f}%)")
else:
    print("\nNo backslash sequences found.")

# Report Lone Backslashes
if lone_backslashes:
    print("\nLone backslashes found at the following positions:")
    for item in lone_backslashes:
        print(f"Row {item['index']} in column '{item['column']}', context: '{item['context']}'")
else:
    print("\nNo lone backslashes found.")

# -----------------------------
# Step 6: Quotation Marks Analysis
# -----------------------------

total_questions = len(df)
questions_start_end_quotes = 0
questions_contain_quotes = 0
questions_triple_quotes = 0
questions_double_quotes_inside = 0

triple_quotes_positions = []

for idx, question in df['question'].dropna().items():
    question = str(question)
    starts_with_quote = question.startswith('"')
    ends_with_quote = question.endswith('"')
    contains_triple_quotes = '"""' in question
    contains_double_quotes_inside = '""' in question.replace('"""', '')  # Exclude triple quotes

    if starts_with_quote and ends_with_quote:
        questions_start_end_quotes += 1
    if contains_triple_quotes:
        questions_triple_quotes += 1
        triple_quotes_positions.append({'index': idx, 'question': question})
    if '"' in question:
        questions_contain_quotes += 1
    if contains_double_quotes_inside:
        questions_double_quotes_inside += 1

print(f"\nTotal questions: {total_questions}")
print(f"Questions starting and ending with quotes: {questions_start_end_quotes}")
print(f"Questions containing triple quotes: {questions_triple_quotes}")
print(f"Questions containing quotes inside: {questions_contain_quotes}")
print(f"Questions containing double quotes inside (excluding triple quotes): {questions_double_quotes_inside}")

if triple_quotes_positions:
    print("\nExamples of questions containing triple quotes:")
    for item in triple_quotes_positions[:5]:  # Display up to 5 examples
        print(f"Row {item['index']}: {item['question']}")

# -----------------------------
# Step 8: Implementing Quote Standardization
# -----------------------------

def clean_quotes(question):
    if pd.isnull(question):
        return question
    question = str(question).strip()
    # Remove outer quotes if they exist
    if question.startswith('"') and question.endswith('"'):
        question = question[1:-1].strip()
    # Replace triple quotes with single quotes
    question = question.replace('"""', '"')
    # Replace doubled quotes inside with single quotes
    question = question.replace('""', '"')
    # Replace escaped quotes
    question = question.replace('\\"', '"').replace("\\'", "'")
    # Remove any remaining backslashes
    question = question.replace('\\', '')
    # Unescape HTML entities
    question = html.unescape(question)
    # Strip again after replacements
    question = question.strip()
    return question

# Apply the function to the 'question' column
df['question'] = df['question'].apply(clean_quotes)

# -----------------------------
# Optional: Re-run Quotation Marks Analysis After Cleaning
# -----------------------------

# You can re-run the quotation marks analysis here if you wish to verify the changes.

# -----------------------------
# Step 10: Save the Cleaned Data
# -----------------------------

# Replace with your desired output file path
df.to_csv('all_data_final_cleaned.tsv', sep='\t', index=False, encoding='utf-8')

print("\nData cleaning and sanity checks completed. Cleaned data saved to 'all_data_final_cleaned.tsv'.")
