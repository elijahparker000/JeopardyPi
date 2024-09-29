import os
import pandas as pd

# Define the function to get Jeopardy clues
def get_jeopardy_clues(proj_path):
    file_path = os.path.join(proj_path, "clues/jeopardy.csv")
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # Filter the DataFrame for the 'Jeopardy!' round and remove duplicates of categories
    show_round_category = df[['Show Number', 'Round', 'Category']]
    df_show_list = show_round_category.drop_duplicates()
    df_jeopardy = df_show_list[df_show_list['Round'] == 'Jeopardy!']

    # Randomly sample 6 categories
    df_jeopardy_sampled = df_jeopardy.sample(n=6)

    # Merge the sampled categories with the original dataframe to get the clues and answers
    df_jeopardy_active_clues = pd.merge(
        df, 
        df_jeopardy_sampled, 
        on=['Show Number', 'Round', 'Category'], 
        how='inner'
    )

    # Extract the categories, questions, answers, and values for the selected categories
    categories = df_jeopardy_sampled['Category'].tolist()  # List of selected categories

    # For each category, get the corresponding clues and answers
    clues = {}
    for category in categories:
        clues_for_category = df_jeopardy_active_clues[df_jeopardy_active_clues['Category'] == category]
        clues[category] = [
            {'clue': clue['Question'], 'response': clue['Answer']}
            for _, clue in clues_for_category.iterrows()
        ]

    return categories, clues




def return_clue_and_response(categories, clues, row, col):
    try:
        category_number = int(col)
        clue_number = int(row)
    except (IndexError, ValueError):
        raise ValueError("Invalid button name format")

    category_name = categories[category_number]
    category_clues = clues.get(category_name)

    if clue_number >= len(category_clues):
        raise ValueError("Invalid clue number")

    selected_clue = category_clues[clue_number]
    return selected_clue['clue'], selected_clue['response']
