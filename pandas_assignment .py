import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})
print(df)

df['From_To'] = df['From_To'].str.title()
print(df.head())

df['FlightNumber'].iloc[1] = 10055
df['FlightNumber'].iloc[3] = 10075
df['FlightNumber'] = df['FlightNumber'].astype(int)
print(df.head())

df1 = df.From_To.str.split("_", expand=True)
pd.DataFrame(df1)
df1.columns=['From', 'To']
print(df1)

df.drop(columns=['From_To'], axis=0, inplace=True)
print(df)

df = df.join(df1, how='outer')
print(df)

delays = pd.DataFrame(df['RecentDelays'].to_list(), columns=['delay_1', 'delay_2', 'delay_3'])
print(delays)

df = df.join(delays, how='outer')
df.drop(columns=['RecentDelays'], axis=0, inplace=True)
print(df)
