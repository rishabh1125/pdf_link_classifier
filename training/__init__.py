import pandas as pd


df = pd.read_excel('data/DataSet.xlsx')
print(len(df),'\n',df['datasheet_link'][0])

