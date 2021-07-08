import numpy as np

print('empty np array')
empty_array = np.array(None)
print(empty_array)

print('filled with zeros')
filled_with_zeros = np.zeros(3, dtype=int)
print(filled_with_zeros)

print('filled with ones')
filled_with_ones = np.ones(3, dtype=int)
print(filled_with_ones)

print('filled with lists')
np_full_array = np.full((3, 2), 2)
print(np_full_array)

print("checks whether np array contains row")
np_full_array[1] = [3, 1]
print([3, 2] in np_full_array.tolist())

print('generating string np array to value')
number = 10
array_with_str = np.genfromtxt(np.array([10, 'alelo', number, 1.3]))
print(array_with_str)

print('removed the nan values')
without_nan_values = array_with_str[np.logical_not(np.isnan(array_with_str))]
print(without_nan_values)

arr = [1, 3, 2], [1, 3, 45], [3]

print('Created simple array')
messed_dimensions = np.array(arr)
print(messed_dimensions)
print(np.squeeze(messed_dimensions))