import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('JeopardyTeenQs.xlsx', sheet_name='Sheet1', header=None)
num_rows = df.shape[0]
print(num_rows)


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

