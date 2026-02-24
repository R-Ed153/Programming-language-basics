import pandas as pd
import numpy as np

df = pd.DataFrame({"a": [10, 20, 30], "b": [20, 30, 40]})

@np.vectorize
def avg_2_mod(x, y):
    if x == 20:
        return np.nan
    else:
        return (x + y) / 2
    
avg_2_mod_vec = np.vectorize(avg_2_mod)


print(avg_2_mod(10,20))
print(avg_2_mod(20,30))
print(avg_2_mod(df['a'],df['b']))
print(avg_2_mod_vec(df['a'],df['b']))