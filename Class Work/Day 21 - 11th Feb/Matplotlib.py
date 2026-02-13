import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[6,7,8,9,10])
#plt.show()

x = [1,2,3,4,5]
y = [10,18,25,42,55]
plt.plot(x,y, marker='o', linestyle='solid', color='red')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line Chart')
plt.grid(True)
plt.show()

name=["A","B","C","D"]
scores= [75,85,95,105]
plt.bar(name,scores)
plt.title('Student Scores')
plt.show()

plt.barh(name,scores)
plt.show()

plt.scatter(name,scores)
plt.show()

marks = [67,78,72,85,98]
plt.hist(marks,bins=20)
plt.title("Marks")
plt.show()

labels = ["Chrome","firefox","Edge"]
sizes = [80,60,30]
plt.pie(sizes,labels=labels,autopct='%1.2f%%')
plt.title("Browser Usage")
plt.show()