import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")
print(tips)

colors = {"Female": "#f1a340", "Male": "#998ec3"}

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)

axes1.scatter(
    data=tips,
    x="total_bill",
    y="tip",
    s=tips["size"] ** 2 * 10,
    c=tips["sex"].map(colors),
    alpha=0.5,
)


axes1.set_title("Colored by Sex and Sized by Size")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")

scatter_plot.suptitle("Total Bill vs Tip")

plt.show()
