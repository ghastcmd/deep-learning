import numpy as np

# Empty np array
empty_array = np.array(None)
print(empty_array)

# Array filled with zeroes
filled_with_zeros = np.zeros(3, dtype=int)
print(filled_with_zeros)

# Array filled with ones
filled_with_ones = np.ones(3, dtype=int)
print(filled_with_ones)

# Array filled with lists
np_full_array = np.full((3, 2), 2)
print(np_full_array)

# If np array contains given row
np_full_array[1] = [3, 1]
print([3, 2] in np_full_array.tolist())

# Generating string np array to value (integers)
number = 10
array_with_str = np.genfromtxt(np.array([10, 'alelo', number, 1.3]))
print(array_with_str)

# Removing NaN values from array
without_nan_values = array_with_str[np.logical_not(np.isnan(array_with_str))]
print(without_nan_values)

# Remove single dimensional entries from the shape of an array
arr = [[1, 4, 2, 3, 1]]
messed_dimensions = np.array(arr)
print(messed_dimensions.squeeze())