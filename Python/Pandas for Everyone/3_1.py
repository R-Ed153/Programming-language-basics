import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")


dataset_1 = anscombe[anscombe['dataset'] == "I"]
plt.plot(dataset_1['x'],dataset_1['y'])
plt.show()
dataset_2 = anscombe[anscombe['dataset'] == "II"]
plt.plot(dataset_1['x'],dataset_1['y'])
plt.show()
dataset_3 = anscombe[anscombe['dataset'] == "III"]
plt.plot(dataset_1['x'],dataset_1['y'])
plt.show()
dataset_4 = anscombe[anscombe['dataset'] == "IV"]
plt.plot(dataset_4['x'],dataset_1['y'],'p')
plt.show()