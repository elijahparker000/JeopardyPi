import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Paths to your TSV files
season1_39_file = os.path.join(proj_path, "clues/all-clues/combined_season1-39.tsv")
extra_games_file = os.path.join(proj_path, "clues/all-clues/extra_matches.tsv")

# Output file path
output_file = os.path.join(proj_path, "clues/all-clues/all_data.tsv")

# Read the 'season1-39' TSV file
print("Reading the 'season1-39' TSV file...")
df_main = pd.read_csv(season1_39_file, sep='\t', encoding='utf-8')

# Read the 'extra games' TSV file
print("Reading the 'extra games' TSV file...")
df_extra = pd.read_csv(extra_games_file, sep='\t', encoding='utf-8')

# Concatenate the two DataFrames
print("Concatenating the DataFrames...")
df_combined = pd.concat([df_main, df_extra], ignore_index=True)

# Save the combined DataFrame to a TSV file
print(f"Saving the combined data to '{output_file}'...")
df_combined.to_csv(output_file, sep='\t', index=False, encoding='utf-8')

print("Done!")
