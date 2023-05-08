import pandas as pd
import random as rand

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('Questions/testAfterDrop.xlsx', sheet_name='Sheet1', header=None)
num_rows = df.shape[0]
#print(num_rows)

index = rand.randrange(0, num_rows)
print(index)
print(df.iloc[index, 1])


#subset_df = df.iloc[0:10, 3:7]
#print(df.iloc[1, 3])
#print(df.iloc[6, 3])
#print(df.iloc[11, 3])
#print(df.iloc[16, 3])
#print(df.iloc[21, 3])
#print(df.iloc[26, 3])
#print(df)

#remove first four rows
#df = df.drop([0, 1, 2, 3])
#print(df)

#save to excel
#df.to_excel('C:/Users/elija/OneDrive/Desktop/PythonScripts/JeopardyProjectRepo/JeopardyPi/testAfterDrop.xlsx', sheet_name='Sheet1', index=False, header=None)

