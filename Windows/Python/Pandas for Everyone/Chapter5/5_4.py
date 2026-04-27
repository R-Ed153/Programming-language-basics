import pandas as pd

df = pd.DataFrame({"a":[10,20,30],"b":[20,30,40]})

df["a_sq_lamb"] = df["a"].apply(lambda x:x ** 2)

print(df)