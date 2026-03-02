import seaborn as sns
from numpy.random import SeedSequence,permutation
import numpy as np


rs = SeedSequence()
rs1 = SeedSequence(rs.entropy)

tips_10 = sns.load_dataset("tips").sample(10)
tips_10.loc[permutation(tips_10.index[:4]),"total_bill"] = np.nan

#print(tips_10)

count_sex = tips_10.groupby('sex').count()
#print(count_sex)

def fill_na_mean(x):
    avg = x.mean()
    return x.fillna(avg)

total_bill_group_mean = (
    tips_10.groupby("sex").total_bill.transform(fill_na_mean)
)

tips_10["fill_total_bill"] = total_bill_group_mean

print(tips_10[["sex","total_bill","fill_total_bill"]])