import pandas as pd

df = pd.DataFrame({"a":[10,20,30],"b":[20,30,40]})

def my_exp(x,e):
    return x ** e

#print(df['a'].apply(my_exp,e=2))

def print_me(x):
    print(x)

df.apply(print_me,axis=1)