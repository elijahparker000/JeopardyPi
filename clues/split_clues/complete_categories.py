import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

# Load the 'Easy.csv' file
csv_file = os.path.join(proj_path, "clues/split_clues/expert.csv")  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Ensure 'round' column is of integer type
df['round'] = df['round'].astype(int)

# Strip whitespace from 'category' names and convert to uppercase for consistency
df['category'] = df['category'].str.strip().str.upper()

# Function to filter complete categories in rounds 1 and 2
def filter_complete_categories(df):
    # Filter for rounds 1 and 2
    df_rounds = df[df['round'].isin([1, 2])]

    # Group by 'round', 'air_date', and 'category', count the number of clues in each group
    category_counts = df_rounds.groupby(['round', 'air_date', 'category']).size().reset_index(name='counts')

    # Select categories with exactly 5 clues
    complete_categories = category_counts[category_counts['counts'] == 5]

    # Merge back to get only clues from complete categories
    df_complete = pd.merge(df_rounds, complete_categories[['round', 'air_date', 'category']], on=['round', 'air_date', 'category'], how='inner')

    # For round 3 (Final Jeopardy), we can choose to keep or discard clues
    # Here, we'll keep them
    df_round3 = df[df['round'] == 3]

    # Combine the filtered rounds 1 and 2 with round 3
    df_filtered = pd.concat([df_complete, df_round3], ignore_index=True)

    return df_filtered

# Apply the filtering function
df_filtered = filter_complete_categories(df)

# Save the filtered DataFrame back to 'Easy.csv' or to a new file
output_file = 'expert_filtered.csv'  # Change to 'Easy.csv' to overwrite the original file
df_filtered.to_csv(output_file, index=False)

print("Filtering complete. The filtered data is saved to", output_file)
