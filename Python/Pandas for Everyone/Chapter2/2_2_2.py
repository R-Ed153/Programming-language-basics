import pandas as pd

scientists = pd.read_csv("data/scientists.csv")

ages = scientists["Age"]
print(ages.sample(2))

print(ages[ages < ages.median()])

print(scientists.values)