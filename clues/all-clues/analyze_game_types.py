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
    r'\bTeen\b', # Easy
    r'\bCollege Championship\b', # Medium
    r'\bTournament of Champions\b', # Expert
    r'\bTeachers Tournament\b', # Medium
    r'\bKids Week\b', # Easy
    r'\bCelebrity\b', # Easy
    r'\bSeniors?\b', # Medium
    r'\bBattle of the Decades\b', # TOC Level (Expert)
    r'\bAll-Star Games\b', # TOC Level (Expert)
    r'\bPower Players Week\b', # Equivalent to Celebrity Jeopardy (Easy)
    r'\bArmed Forces\b', # Medium
    r'\bBoston\b', # exclude 
    r'\bInternational\b', # exclude
    r'\bBack to School\b', # Easy
    r'\b10th Anniversary\b', # TOC Level (Expert)
    r'\bOlympic\b', # exclude
    r'\bMillion Dollar Masters\b', # TOC Level (Expert)
    r'\bIBM\b', # TOC Level (Expert)
    r'^-$' #normal games (Hard)
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

total=0
for game_type, count in game_type_counts.items():
    total=total+count
print(f"{total} Total Clues")
