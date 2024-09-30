import pandas as pd
import re
from collections import Counter
from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Load the CSV file
csv_file = os.path.join(proj_path, "clues/all-clues/AllClues-350000.csv")  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Extract the 'notes' column and drop NaN values
notes_series = df['notes'].dropna()

# Initialize a list to hold all game type mentions
game_types = []

# Define patterns to look for common game types
game_type_patterns = [
    r'\bTeen Tournament\b',
    r'\bCollege Championship\b',
    r'\bTournament of Champions\b',
    r'\bTeachers Tournament\b',
    r'\bKids Week\b',
    r'\bCelebrity Jeopardy\b',
    r'\bSeniors Tournament\b',
    r'\bBattle of the Decades\b',
    r'\bAll-Star Games\b',
    r'\bPower Players Week\b',
    # Add more patterns as needed
]

# Compile regex patterns
compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in game_type_patterns]

# Process each note
for note in notes_series:
    for pattern in compiled_patterns:
        match = pattern.search(note)
        if match:
            game_types.append(match.group())

# Count the occurrences of each game type
game_type_counts = Counter(game_types)

# Display the unique game types and their counts
print("Unique Game Types Found:")
for game_type, count in game_type_counts.items():
    print(f"{game_type}: {count} occurrences")

# Optionally, display notes that didn't match any known game type
unknown_notes = []
for note in notes_series:
    if not any(pattern.search(note) for pattern in compiled_patterns):
        unknown_notes.append(note)

if unknown_notes:
    print("\nNotes without recognized game types:")
    for note in set(unknown_notes):
        print(note)
