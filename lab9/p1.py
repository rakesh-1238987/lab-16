import pandas as pd

# Define two series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("Series 1:")
print(s1)
print("Series 2:")
print(s2)

print("\nAddition:")
print(s1 + s2)

print("\nSubtraction:")
print(s1 - s2)

print("\nMultiplication:")
print(s1 * s2)

print("\nDivision:")
print(s1 / s2)
