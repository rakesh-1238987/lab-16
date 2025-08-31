import pandas as pd
import numpy as np

# From List
list_data = [10, 20, 30, 40]
series_list = pd.Series(list_data)
print("Series from List:")
print(series_list)

# From Numpy Array
array_data = np.array([1, 2, 3, 4])
series_array = pd.Series(array_data)
print("\nSeries from Numpy Array:")
print(series_array)

# From Dictionary
dict_data = {'x': 100, 'y': 200, 'z': 300}
series_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:")
print(series_dict)
