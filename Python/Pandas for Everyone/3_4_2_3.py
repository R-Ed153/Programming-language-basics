import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")

hexbin = sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex")
hexbin.set_axis_labels(xlabel = "Total Bill", ylabel="Tip")
hexbin.figure.suptitle("Hexbin Plot of Total Bill and Tip", y=1.03)
 
plt.show()