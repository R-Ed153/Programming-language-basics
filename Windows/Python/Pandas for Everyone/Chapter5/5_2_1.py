import pandas as pd

df = pd.DataFrame({"a":[10,20,30],"b":[20,30,40]})

print(type(df['a']))
print(type(df.iloc[1]))