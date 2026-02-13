import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# Matplotlib Line Chart
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Seaborn Bar Plot
plt.figure()
sns.barplot(x=months, y=sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
