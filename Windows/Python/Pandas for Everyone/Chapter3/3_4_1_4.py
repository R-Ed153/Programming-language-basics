import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")
fig = sns.displot(data = tips, x = "total_bill", kde = True, rug = True)
fig.set_axis_labels(x_var="Total Bill", y_var="Count")
fig.figure.suptitle("Distribution of Total Bill")

plt.show()