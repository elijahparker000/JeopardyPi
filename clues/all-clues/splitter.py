import pandas as pd
import re
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Load the original CSV file
csv_file = os.path.join(proj_path, "clues/all-clues/AllClues-350000.csv")  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Define the regex patterns and their associated difficulty levels
pattern_difficulty = [
    (r'\bTeen\b', 'Easy'),                      # Easy
    (r'\bCollege Championship\b', 'Medium'),    # Medium
    (r'\bTournament of Champions\b', 'Expert'), # Expert
    (r'\bTeachers Tournament\b', 'Medium'),     # Medium
    (r'\bKids Week\b', 'Easy'),                 # Easy
    (r'\bCelebrity\b', 'Easy'),                 # Easy
    (r'\bSeniors?\b', 'Medium'),                # Medium
    (r'\bBattle of the Decades\b', 'Expert'),   # Expert
    (r'\bAll-Star Games\b', 'Expert'),          # Expert
    (r'\bPower Players Week\b', 'Easy'),        # Easy (Equivalent to Celebrity Jeopardy)
    # Exclude 'Boston', 'International', 'Olympic', 'Armed Forces' (do not include these in patterns)
    (r'\bBack to School\b', 'Easy'),            # Easy
    (r'\b10th Anniversary\b', 'Expert'),        # Expert
    (r'\bMillion Dollar Masters\b', 'Expert'),  # Expert
    (r'\bIBM\b', 'Expert'),                     # Expert
    (r'^-$', 'Hard')                            # Hard (normal games)
]

# Compile the regex patterns
compiled_patterns = [(re.compile(pattern, re.IGNORECASE), difficulty) for pattern, difficulty in pattern_difficulty]

# Function to classify each note based on the patterns
def classify_difficulty(note):
    for pattern, difficulty in compiled_patterns:
        if pattern.search(note):
            return difficulty
    return None  # Return None if no pattern matches (these will be excluded)

# Replace NaN in 'notes' with '-' to represent normal games
df['notes'] = df['notes'].fillna('-')

# Apply the classification to the DataFrame
df['Difficulty'] = df['notes'].apply(classify_difficulty)

# Exclude rows with game types that are to be excluded (where Difficulty is None)
df = df[df['Difficulty'].notnull()]

# Split the DataFrame into separate DataFrames for each difficulty level
df_easy = df[df['Difficulty'] == 'Easy']
df_medium = df[df['Difficulty'] == 'Medium']
df_hard = df[df['Difficulty'] == 'Hard']
df_expert = df[df['Difficulty'] == 'Expert']

# Define the output directory (you can change this as needed)
output_dir = os.path.join(proj_path, "clues/split_clues")
os.makedirs(output_dir, exist_ok=True)

# Save each DataFrame to a separate CSV file
df_easy.to_csv(os.path.join(output_dir, 'easy.csv'), index=False)
df_medium.to_csv(os.path.join(output_dir, 'medium.csv'), index=False)
df_hard.to_csv(os.path.join(output_dir, 'hard.csv'), index=False)
df_expert.to_csv(os.path.join(output_dir, 'expert.csv'), index=False)

print("Clues have been split into difficulty levels and saved to CSV files.")
