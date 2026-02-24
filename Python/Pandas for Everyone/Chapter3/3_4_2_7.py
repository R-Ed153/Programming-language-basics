import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")
print(tips)
violin,ax = plt.subplots()

sns.violinplot(data=tips, x="time", y="total_bill", hue="sex", split="False",ax=ax)

ax.set_title("Violin plot of total bill by time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Total Bill")

plt.show()