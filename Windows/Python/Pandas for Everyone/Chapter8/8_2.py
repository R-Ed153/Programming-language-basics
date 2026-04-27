import pandas as pd


df = pd.read_csv("data/gapminder.tsv",sep="\t")

def myZcore(x):
    return ((x-x.mean())/x.std())

transform_z = df.groupby('year')["lifeExp"].transform(myZcore)
print(transform_z)