import matplotlib.pyplot as plt

# Sample Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Plot bar chart
plt.bar(languages, popularity, color=['blue', 'green', 'red', 'purple', 'orange', 'cyan'])

# Labels and Title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

plt.show()
