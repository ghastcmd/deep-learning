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

# Finding the number of rows and columns for a given matrix
print('rows=', mat.shape[0], 'columns=', mat.shape[1])

# Create a slice from a given matrix
s_slice = mat[2,2:]
print(s_slice)

# Finding the sum of values of a matrix
print(mat.sum())

# Finding the sum of diagonal of a matrix
print(mat.diagonal().sum())

# Adding or subtracting matrices in python
mat2 = np.matrix(np.random.randint(24, size=12).reshape(3, 4))
mat3 = mat + mat2
print(mat3)

# Ways to add row/column in np array
mat = np.concatenate((mat, np.array([[1,2,3,4]])))
mat = np.concatenate((mat, np.vstack([1,2,3,4])), axis=1)
print(mat)

# Multiply matrices in python
mat2 = mat2.T * mat3
print(mat2)

# Get aigen values for a given matrix
print(np.linalg.eigvals(mat2))

# Determinant of matrix using np
print(np.linalg.det(mat2))

# Inverse of matrix using np
print(np.linalg.inv(mat2))

# Frequency of unique values inside of matrix
mat2 = np.matrix(np.random.randint(4, size=12).reshape(3, 4))
unique = np.unique(mat2)
print(unique)

# Multiply matrices of complex numbers using NumPy in Python
first = np.array([[2 + 1j, 1 + 2j], [1, 2 + 4j]])
second = np.array([[1 + 2j, 2 + 1j], [2 - 1j, 2 - 2j]])
third = np.dot(first, second)
print(third)

# Outer product of two given vectors using NumPy
first = np.arange(4)
second = np.random.randint(3, size=4)
third = np.outer(first, second)
print(third)

# Inner, outer and cross product
mat = np.matrix(np.arange(16).reshape(4, 4))
print('Different products mats')
print(mat, '\n', third)
print(np.inner(mat, third))
print(np.cross(mat.reshape(-1, 2), third.reshape(-1, 2)))

# Calculate the covariance matrix from two given arrays
print(first, second)
cov_mat = np.cov(first, second)
print(cov_mat)

# Convert covariance matrix to correlation matrix
print(np.corrcoef(cov_mat))

# Compute the kronecker product of two multidimension matrix
print(np.kron(mat, np.corrcoef(cov_mat)))

# Convert matrix into a list
first_list = mat2.ravel().tolist()
print(first_list)

##### Numpy Indexing #####

# Convert all values that doesn't satisfy the rule
first[first < 2] = 0
print(first)

# Return the indices of elements where the given condition is satisfied
indices = np.where(first > 2)[0]
print(indices)

# Replace NaN values with mean values of columns
first = np.arange(30, dtype=float).reshape(5, 6)
first[3,0:2] = np.NaN
inds = np.where(np.isnan(first))
first[inds] = np.take(np.nanmean(first, axis=0), inds[1])
print(first)