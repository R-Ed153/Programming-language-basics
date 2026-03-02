import seaborn as sns

tips_10 = sns.load_dataset("tips").sample(10,random_state=42)
#print(tips_10)

#grouped = tips_10.groupby('sex')

#print(grouped.get_group("Female"))

#for sex_group in grouped:
    #print(sex_group[0])
    #pass

bill_sex_time = tips_10.groupby(["sex","time"],observed=False)
print(bill_sex_time.count())