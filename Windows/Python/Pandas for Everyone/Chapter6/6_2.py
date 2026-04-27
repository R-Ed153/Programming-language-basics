import pandas as pd

df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')

row_concat = pd.concat([df1,df2,df3],ignore_index=True)
print(row_concat)

new_row_series =  pd.DataFrame(data=[['n1','n2','n3','n4']],columns=["A","B","C","D"])
#print(new_row_series)

print(pd.concat([row_concat,new_row_series]))