import pandas as pd
from tqdm import tqdm
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Paths to your TSV files
# Replace these with the actual paths to your files
season1_39_file = os.path.join(proj_path, "clues/all-clues/combined_season1-39.tsv")
extra_games_file = os.path.join(proj_path, "clues/all-clues/extra_matches.tsv")

# Read the 'season1-39' TSV file
print("Reading the 'season1-39' TSV file...")
df_main = pd.read_csv(season1_39_file, sep='\t', encoding='utf-8')

# Read the 'extra games' TSV file
print("Reading the 'extra games' TSV file...")
df_extra = pd.read_csv(extra_games_file, sep='\t', encoding='utf-8')

# Preprocess the 'answer' columns
def preprocess_answer(answer):
    # Convert to string, lower case, and strip leading/trailing whitespace
    return str(answer).strip().lower()

# Create a set of unique preprocessed answers from the main dataset
print("Creating a set of unique answers from the 'season1-39' file...")
main_answers_set = set(df_main['answer'].apply(preprocess_answer))

# Initialize a list to store duplicates
duplicates = []

# Iterate over the 'answer' column in the 'extra games' DataFrame with a progress bar
print("Checking for duplicates...")
for idx, row in tqdm(df_extra.iterrows(), total=df_extra.shape[0]):
    extra_answer = preprocess_answer(row['answer'])
    if extra_answer in main_answers_set:
        # Duplicate found
        duplicates.append({
            'index': idx,
            'answer': row['answer'],
            'question': row['question'],
            'category': row['category'],
            'air_date': row['air_date'],
            'notes': row['notes']
        })

# Convert duplicates list to a DataFrame
duplicates_df = pd.DataFrame(duplicates)

# Output the duplicates
if not duplicates_df.empty:
    print(f"\nFound {len(duplicates_df)} duplicate answers:")
    print(duplicates_df[['index', 'answer', 'question', 'category', 'air_date', 'notes']])
    # Optionally, save the duplicates to a CSV file
    duplicates_df.to_csv('duplicate_answers.csv', index=False)
    print("\nDuplicate answers have been saved to 'duplicate_answers.csv'.")
else:
    print("\nNo duplicate answers found.")
