import pandas as pd

ebola = pd.read_csv('data/country_timeseries.csv')
#print(ebola.columns)

ebola_long = ebola.melt(id_vars=["Date","Day"])
#print(ebola_long)

status_values = ebola_long["variable"].str.split("_").str.get(0)
country_values = ebola_long["variable"].str.split("_").str.get(1)

ebola_long["status_values"] = status_values
ebola_long["country_values"] = country_values

print(ebola_long)