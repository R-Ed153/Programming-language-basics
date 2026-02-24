import pandas as pd

scientists = pd.read_csv("data/scientists.csv")

print(type(scientists.loc[scientists['Age'] > scientists['Age'].mean()]))
print(type(scientists.loc[[2,3]]))