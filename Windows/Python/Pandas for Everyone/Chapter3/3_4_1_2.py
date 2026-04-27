import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")
print(tips)

den,ax = plt.subplots()

sns.kdeplot(data=tips, x="total_bill", ax=ax)
sns.rugplot(data=tips,x="total_bill",ax=ax)

ax.set_title("Total Bill Density")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Unit Probability")

plt.show()