import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]
y3 = [1, 8, 27, 64, 125]

# Plot multiple lines
plt.plot(x, y1, label="y = 2x")
plt.plot(x, y2, label="y = x²")
plt.plot(x, y3, label="y = x³")

# Labels, Title, and Legend
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Line Graphs")
plt.legend()

plt.show()
