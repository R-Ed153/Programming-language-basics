import pandas as pd

ebola = pd.read_csv('data/country_timeseries.csv')
#print(ebola.columns)

ebola_long = ebola.melt(id_vars=["Date","Day"])

variable_split = ebola_long.variable.str.split('_',expand=True)
#print(variable_split)

ebola_long[['status','country']] = variable_split
print(ebola_long)