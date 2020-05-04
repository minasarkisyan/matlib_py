import matplotlib.pyplot as plt

x_2_values = list(range(1001))
y_2_values = [x**2 for x in x_2_values]
y_3_values = [x**3 for x in x_2_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_2_values, y_2_values, c=y_2_values, cmap=plt.cm.Blues, s=10)
ax.scatter(x_2_values, y_3_values, c=y_3_values, cmap=plt.cm.Greens, s=20)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

plt.show()