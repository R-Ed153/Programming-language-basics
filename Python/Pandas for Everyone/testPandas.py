import pandas as pd

df = pd.read_csv('./data/gapminder.tsv',sep='\t')

print(type(df))
print(df.shape)
print(type(df.columns))
