import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")

dataset_1 = anscombe[anscombe['dataset'] == "I"]
dataset_2 = anscombe[anscombe['dataset'] == "II"]
dataset_3 = anscombe[anscombe['dataset'] == "III"]
dataset_4 = anscombe[anscombe['dataset'] == "IV"]

figure = plt.figure()

axes1 = figure.add_subplot(2,2,1)
axes2 = figure.add_subplot(2,2,2)
axes3 = figure.add_subplot(2,2,3)
axes4 = figure.add_subplot(2,2,4)

axes1.plot(dataset_1['x'],dataset_1['y'],'o')
axes2.plot(dataset_2['x'],dataset_2['y'],'o')
axes3.plot(dataset_3['x'],dataset_3['y'],'o')
axes4.plot(dataset_4['x'],dataset_4['y'],'o')

axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

figure.suptitle("Anscombe data")
plt.show()