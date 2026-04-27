import pandas as pd

df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')

df1.columns = ["A","B","C","D"]
df2.columns = ["E","F","G","H"]
df3.columns = ["A","C","F","H"]

#print(df1)
#print(df2)
#print(df3)

row_concat = pd.concat([df1,df2,df3],join="inner")
print(row_concat)