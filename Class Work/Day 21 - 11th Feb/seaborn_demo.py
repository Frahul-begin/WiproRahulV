import seaborn as sns
import matplotlib.pyplot as plt

marks=[50,60,70,80,90,65]

sns.histplot(marks,bins=10)
plt.title("Marks")
plt.show()