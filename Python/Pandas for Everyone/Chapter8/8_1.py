import pandas as pd

df = pd.read_csv("data/gapminder.tsv",sep="\t")
avg_life_exp_by_year = df.groupby('year')["lifeExp"].mean()
#print(df.groupby('country')["pop"].std())
print(avg_life_exp_by_year)