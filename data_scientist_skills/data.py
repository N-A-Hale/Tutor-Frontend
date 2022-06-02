import pandas as pd




def get_data():
    #Get data
    ###removing ../ allows terminal command 'make run_locally' to work -JP
    df1 = pd.read_csv("raw_data/DataAnalyst.csv")
    df2 = pd.read_csv("raw_data/DataScientist.csv")
    #Concat to full dataframe
    df = pd.concat([df1, df2], ignore_index=True, axis=0)
    #Drop columns and reformat names
    df.drop(columns=['Unnamed: 0', 'index', 'Revenue', 'Competitors', 'Easy Apply'], inplace=True)
    df.columns = [column.replace(' ', '_').lower() for column in df.columns]
    df.reset_index(drop=True)
    df.drop_duplicates()
    return df
