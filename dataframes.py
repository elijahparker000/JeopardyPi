import random
import pandas as pd

DDtemp = "foo"
cat1NameComp = "foo"
cat2NameComp = "foo"
gameRound = 1
df = pd.read_excel('Questions/JeopardyTeenQs.xlsx', sheet_name='Sheet1', header=None)


if round == 1:
 df = pd.read_excel('Questions/JeopardyTeenQs.xlsx', sheet_name='Sheet1', header=None)
if round == 2:
 df = pd.read_excel('Questions/DoubleJeopardyTeenQs.xlsx', sheet_name='Sheet1', header=None)
num_rows = df.shape[0]

while True:
    #These are which indeces the categories and questions are pulled from the df
    cat1Index = random.randrange(0,num_rows-4,5)
    cat2Index = random.randrange(0,num_rows-4,5)
    cat3Index = random.randrange(0,num_rows-4,5)
    cat4Index = random.randrange(0,num_rows-4,5)
    cat5Index = random.randrange(0,num_rows-4,5)
    cat6Index = random.randrange(0,num_rows-4,5)
    DDcount = 0
    unique = True
    for i in range(1, 7): #for each of the 6 categories
        for j in range(0,5): #for each question within the category
            exec(f'global DDtemp; DDtemp = df.iloc[cat{i}Index + {j}, 2]')
            print(DDtemp)
            if DDtemp == "yes":
                DDcount += 1
    for i in range(1,6):
        for j in range(i+1,7):
            #TODO: these cat1NameComp and cat2NameComp shouldn't have to be global
            exec(f'global cat1NameComp; cat1NameComp = df.iloc[cat{i}Index, 3]')
            exec(f'global cat2NameComp; cat2NameComp = df.iloc[cat{j}Index, 3]')
            #uncomment these print functions to see the comparisons it's making
            #print(cat1NameComp)
            #print(cat2NameComp +"\n\n")
            if(cat1NameComp == cat2NameComp):
                    unique = False
    print("\n\n")
    if(DDcount == gameRound and unique == True):
        df1 = df.iloc[cat1Index:cat1Index+5, :]
        df2 = df.iloc[cat2Index:cat2Index+5, :]
        df3 = df.iloc[cat3Index:cat3Index+5, :]
        df4 = df.iloc[cat4Index:cat4Index+5, :]
        df5 = df.iloc[cat5Index:cat5Index+5, :]
        df6 = df.iloc[cat6Index:cat6Index+5, :]
        
        df = pd.concat([df1, df2, df3, df4, df5, df6])
        print(df)
        del df1
        del df2
        del df3
        del df4
        del df5
        del df6
        print(df.iloc[5, 6])
        break
