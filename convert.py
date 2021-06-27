import pandas as pd

df = pd.read_excel('./data/PASSENGER_RECORD.xlsx')
df['PPID'] = df['PPID'].apply(str).apply(lambda x: '\t' + x)
df['BUYYER_PID'] = df['BUYYER_PID'].apply(str).apply(lambda x: '\t' + x)
df.to_csv('./data/PASSENGER_RECORD.csv')