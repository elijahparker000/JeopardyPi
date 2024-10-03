import pandas as pd
import re
import html
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Load the TSV file
csv_file = os.path.join(proj_path, "clues/all-clues/all_data.tsv")  # Replace with your actual file path

# Read the TSV file
df = pd.read_csv(csv_file, sep='\t', encoding='utf-8', dtype={'round': str})

# Standardize the 'round' column
round_mapping = {
    'single': 1,
    'double': 2,
    'final': 3
}

def standardize_round(value):
    if pd.isnull(value):
        return value
    value_str = str(value).strip().lower()
    if value_str in round_mapping:
        return round_mapping[value_str]
    else:
        try:
            return int(value_str)
        except ValueError:
            return pd.NA

df['round'] = df['round'].apply(standardize_round)
df['round'] = pd.to_numeric(df['round'], errors='coerce').astype('Int64')

# Standardize the 'daily_double_value' column
df['daily_double_value'] = pd.to_numeric(df['daily_double_value'], errors='coerce').fillna(0)
df['daily_double_value'] = df['daily_double_value'].apply(lambda x: 0 if x == 0 else 1).astype(int)

# Clean up text formatting
def clean_text(text):
    if pd.isnull(text):
        return text
    text = str(text)
    text = text.replace('\"\"\"', '"').replace('\"\"', '"')
    text = text.replace("\\\"", '"')
    text = html.unescape(text)
    text = text.strip()
    return text

text_columns = ['category', 'comments', 'answer', 'question', 'notes']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].apply(clean_text)

# Save the cleaned DataFrame to a TSV file
df.to_csv('all_data_cleaned.tsv', sep='\t', index=False, encoding='utf-8')
