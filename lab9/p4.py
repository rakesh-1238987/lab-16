import pandas as pd

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

# Vertical stacking (just concatenation)
vertical_stack = pd.concat([s1, s2], ignore_index=True)
print("Vertical Stack:")
print(vertical_stack)

# Horizontal stacking (side by side as DataFrame)
horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:")
print(horizontal_stack)
