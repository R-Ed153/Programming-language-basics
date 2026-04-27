import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.shape)

print(tips["size"].value_counts(normalize=False))

tips_filtered = (tips.groupby("size").filter(lambda x:x["size"].count()>=30))

print(tips_filtered)