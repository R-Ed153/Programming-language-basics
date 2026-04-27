import pandas as pd
pew = pd.read_csv('data/pew.csv')

#print(pew.iloc[:,0:5])

pew_long = pew.melt(id_vars="religion")
print(pew_long)