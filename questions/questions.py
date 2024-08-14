# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:47:49 2024

@author: me
"""
import pandas as pd

# Specify the path to your file
file_path = r"C:\Elijah\JeopardyPi\questions\jeopardy.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# If column names have leading/trailing spaces, strip them
df.columns = df.columns.str.strip()

# Select the specified columns
show_round_category = df[['Show Number', 'Round', 'Category']]

# Drop duplicates to keep only unique rows
df_show_list = show_round_category.drop_duplicates()


# Filter the DataFrame where 'Round' equals 'Jeopardy!'
df_jeopardy = df_show_list[df_show_list['Round'] == 'Jeopardy!']

# Randomly sample six unique combinations
df_jeopardy_sampled = df_jeopardy.sample(n=6, random_state=42)  # random_state is for reproducibility


# Merge the original DataFrame with the sampled_df to get all matching rows
df_jeopardy_active_questions = pd.merge(df, df_jeopardy_sampled, on=['Show Number', 'Round', 'Category'], how='inner')
print(df_jeopardy_active_questions)
print('done')
