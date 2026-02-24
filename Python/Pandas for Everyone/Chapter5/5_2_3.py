import pandas as pd

def avg_2_apply(row):
    x = row[0]
    y = row[1]
    print(y)
    return (x+y)/2

df = pd.DataFrame({"a": [10, 20, 30], "b": [20, 30, 40]})
print(df)

print(df.apply(avg_2_apply))
