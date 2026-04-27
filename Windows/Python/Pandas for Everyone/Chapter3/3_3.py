import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips)

fig = plt.figure()

axes1= fig.add_subplot(1,1,1)
axes1.hist(data=tips,x="total_bill",bins=15)

axes1.set_title('Histogram of Total Bill')
axes1.set_xlabel("Frequency")
axes1.set_ylabel("Total Bill")

plt.show()
