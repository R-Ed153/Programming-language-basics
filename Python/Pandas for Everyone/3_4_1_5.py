import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset("tips")

count, ax = plt.subplots()

sns.countplot(data = tips, x='day', palette="viridis", ax=ax)
ax.set_title("Count of Days")
ax.set_xlabel("Day of Week")
ax.set_ylabel("Frequency")

plt.show()