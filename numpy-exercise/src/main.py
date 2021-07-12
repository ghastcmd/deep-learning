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
arr = [[1, 4, 2, 3, 3, 1, 2, 3, 1, 3, 3, 3]]
messed_dimensions = np.array(arr)
print(messed_dimensions.squeeze())

# Finding the occurencies of a sequence in np array
print(repr(messed_dimensions).count('2, 3'))

# Finding the most frequent value in np array
curarr = messed_dimensions.squeeze()
print(np.bincount(curarr).argmax())

# Combining a two and one dimensional np array
one_dim = np.array([1])
two_dim = np.array([1, 2])
print(np.concatenate([one_dim, two_dim]))

# Create combinatory interpolation from two np arrays
first_array = np.array([1, 3, 4])
second_array = np.array([6, 7])
fulled_array = np.array(np.meshgrid(second_array, first_array))
fulled_array = fulled_array.reshape(-1, fulled_array[0].size).T
print(fulled_array)

# Adding border around np array
border_array = np.ones((2,2))
border_array = np.pad(border_array, pad_width=1, mode='constant', constant_values=0)
print(border_array)

# How to compare two np arrays
first_array = np.ones(3)
second_array = np.ones(3)
second_array[1] = -1
print(np.array_equal(first_array, second_array))

# Wether values ara in array
print(-1 in second_array)

# Get 2D diagonals from 3D array
arr = np.arange(3 * 3 * 3).reshape(3, 3, 3)
diag_arr = np.diagonal(arr, axis1 = 1, axis2 = 2)
print(diag_arr)

# Flatten matrix into array
m = np.matrix([[1,2,3], [4,5,6]])
print(m.flatten())

# Flatten 2d np array into 1d array
flatten_arr = arr.reshape(1, -1)
print(flatten_arr)

# Move axes of an array to new position
arr = np.zeros((2, 2, 1))
print(arr)
print(np.moveaxis(arr, 0, -1))

# Interchange two axis of an array
arr = np.ones((2, 2, 1))
changed_axis = np.swapaxes(arr, 0, -1)
print(arr)
print(changed_axis)

# First 10 numbers using binet formula to find fibonacci
sqrt5 = np.sqrt(5)
alpha = (1 + sqrt5) / 2
beta = (1 - sqrt5) / 2
arrn = np.arange(1, 11)
Fn = ((alpha ** arrn) - (beta ** arrn)) / sqrt5
print(Fn)

# Count the number of non-zero values in the array
first = np.ones(11)
first[6:9] = 0
print(np.count_nonzero(first))

# Counts the number of elements to a given axis
axis = 0
arr = np.array([[1, 2, 3], [3, 4, 5]])
print(np.size(arr, axis))

# Trim the trailing zeros from 1d array
print(first)
first[:2] = 0
first[8:] = 0
print(np.trim_zeros(first))

# Change datatype for a given np array
first.dtype = int
print(first.dtype)
first.dtype = float

# Reverse a numpy array
print(first[::-1])

# Make np array read only
first.flags.writeable = False
print(first)



###### Matrices ######

# Getting the maximum value for a given matrix
np.random.seed(0)
mat = np.matrix(np.random.randint(24, size=12).reshape(3, 4))
print(mat.max())

# Getting the minimun value for a given matrix
print(mat.min())