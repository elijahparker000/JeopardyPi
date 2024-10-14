import pandas as pd
import re
from collections import Counter
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Load the TSV file
csv_file = os.path.join(proj_path, "clues/all-clues/all_data_cleaned.tsv")  # Replace with your actual file path
df = pd.read_csv(csv_file, sep='\t')

# Extract the 'notes' column without dropping NaN values
notes_series = df['notes']

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
    r'\bArmed Forces\b', # Exclude
    r'\bBoston\b', # Exclude 
    r'\bInternational\b', # Exclude
    r'\bBack to School\b', # Easy
    r'\b10th Anniversary\b', # TOC Level (Expert)
    r'\bOlympic\b', # Exclude
    r'\bMillion Dollar Masters\b', # TOC Level (Expert)
    r'\bIBM\b', # TOC Level (Expert)
    r'\bHigh School\b', # Medium
    r'\bProfessors\b', # TOC Level
    r'\bSecond Chance\b', # Exclude
    r'\bAlex Trebek\'s Final Game\b', # Exclude
    r'\bSuper Jeopardy\b', # TOC Level (Expert)
    r'\bMasters\b', # TOC Level (Expert)
    r'\bGreatest of All Time\b', # TOC Level (Expert)
    r'\bPilot\b', # Exclude
]

# Compile regex patterns
compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in game_type_patterns]

# Process each note
for note in notes_series:
    if pd.isnull(note) or note.strip() == '':
        # Note is empty or NaN; count as 'Regular Game'
        game_types.append('Regular Game')
    else:
        matched = False
        for pattern in compiled_patterns:
            match = pattern.search(note)
            if match:
                game_types.append(match.group())
                matched = True
                break
        if not matched:
            # Note didn't match any known game type
            game_types.append('Unknown')

# Count the occurrences of each game type
game_type_counts = Counter(game_types)

# Display the unique game types and their counts
print("Unique Game Types Found:")
for game_type, count in game_type_counts.items():
    print(f"{game_type}: {count} occurrences")

# Optionally, display notes that didn't match any known game type
unknown_notes = []
for idx, note in notes_series.items():
    if pd.isnull(note) or note.strip() == '':
        continue  # Skip regular games
    if not any(pattern.search(note) for pattern in compiled_patterns):
        unknown_notes.append(note)

if unknown_notes:
    print("\nNotes without recognized game types:")
    for note in set(unknown_notes):
        print(note)

# Calculate the total number of clues
total_clues = sum(game_type_counts.values())
print(f"\n{total_clues} Total Clues")

# Optionally, print the total number of Regular Game clues
regular_game_count = game_type_counts.get('Regular Game', 0)
print(f"\nTotal Regular Game Clues: {regular_game_count}")
