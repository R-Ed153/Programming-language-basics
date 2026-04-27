import pandas as pd
df = pd.read_csv("data/gapminder.tsv",sep="\t")


def my_mean(values):
    n = len(values)
    sum = 0

    for value in values:
        sum+=value
    return sum/n

def my_mean_diff(values, diff_value):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    mean = sum/n
    return(mean-diff_value)

global_average = df["lifeExp"].agg(my_mean)

print(global_average)
agg_mean_diff = df.groupby("year")["lifeExp"].agg(my_mean_diff,diff_value = global_average)
print(agg_mean_diff)