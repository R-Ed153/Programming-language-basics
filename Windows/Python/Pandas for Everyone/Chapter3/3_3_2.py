import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 2, 1)
axes2 = scatter_plot.add_subplot(1, 2, 2)

axes1.scatter(data=tips, x="total_bill", y="tip")
axes2.boxplot(
    x=[
        tips.loc[tips["sex"] == "Female", "tip"],
        tips.loc[tips["sex"] == "Male", "tip"],
    ],
    labels = ["Female","Male"]
)

axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")
axes2.set_xlabel("Gender")
axes2.set_ylabel("Tip")

plt.show()