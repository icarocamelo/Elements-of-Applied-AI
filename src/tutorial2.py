import numpy as np
from pandas import Series
import numpy as np

from pandas import DataFrame


oneDim = np.array([1.0,2,3,4,5])   # a 1-dimensional array (vector)
print(oneDim)
print("#Dimensions =", oneDim.ndim)
print("Dimension =", oneDim.shape)
print("Size =", oneDim.size)
print("Array type =", oneDim.dtype, '\n')

twoDim = np.array([[1,2],[3,4],[5,6],[7,8]])  # a two-dimensional array (matrix)
print(twoDim)
print("#Dimensions =", twoDim.ndim)
print("Dimension =", twoDim.shape)
print("Size =", twoDim.size)
print("Array type =", twoDim.dtype, '\n')

arrFromTuple = np.array([(1,'a',3.0),(2,'b',3.5)])  # create ndarray from tuple
print(arrFromTuple)
print("#Dimensions =", arrFromTuple.ndim)
print("Dimension =", arrFromTuple.shape)
print("Size =", arrFromTuple.size)

print('Array of random numbers from a uniform distribution')
print(np.random.rand(5))      # random numbers from a uniform distribution between [0,1]

print('\nArray of random numbers from a normal distribution')
print(np.random.randn(5))     # random numbers from a normal distribution

print('\nArray of integers between -10 and 10, with step size of 2')
print(np.arange(-10,10,2))    # similar to range, but returns ndarray instead of list

print('\n2-dimensional array of integers from 0 to 11')
print(np.arange(12).reshape(3,4))  # reshape to a matrix

print('\nArray of values between 0 and 1, split into 10 equally spaced values')
print(np.linspace(0,1,10))    # split interval [0,1] into 10 equally separated values

print('\nArray of values from 10^-3 to 10^3')
print(np.logspace(-3,3,7))    # create ndarray with values from 10^-3 to 10^3

print('A 2 x 3 matrix of zeros')
print(np.zeros((2,3)))        # a matrix of zeros

print('\nA 3 x 2 matrix of ones')
print(np.ones((3,2)))         # a matrix of ones

print('\nA 3 x 3 identity matrix')
print(np.eye(3))              # a 3 x 3 identity matrix

x = np.array([1,2,3,4,5])

print('x =', x)
print('x + 1 =', x + 1)      # addition
print('x - 1 =', x - 1)      # subtraction
print('x * 2 =', x * 2)      # multiplication
print('x // 2 =', x // 2)     # integer division
print('x ** 2 =', x ** 2)     # square
print('x % 2 =', x % 2)      # modulo  
print('1 / x =', 1 / x)      # division

x = np.array([2,4,6,8,10])
y = np.array([1,2,3,4,5])

print('x =', x)
print('y =', y)
print('x + y =', x + y)      # element-wise addition
print('x - y =', x - y)      # element-wise subtraction
print('x * y =', x * y)      # element-wise multiplication 
print('x / y =', x / y)      # element-wise division
print('x // y =', x // y)    # element-wise integer division 
print('x ** y =', x ** y)    # element-wise exponentiation

x = np.arange(-5,5)
print('Before: x =', x)

y = x[3:5]     # y is a slice, i.e., pointer to a subarray in x
print('        y =', y)
y[:] = 1000    # modifying the value of y will change x
print('After : y =', y)
print('        x =', x, '\n')

z = x[3:5].copy()   # makes a copy of the subarray
print('Before: x =', x)
print('        z =', z)
z[:] = 500          # modifying the value of z will not affect x
print('After : z =', z)
print('        x =', x)

my2dlist = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  # a 2-dim list
print('my2dlist =', my2dlist)
print('my2dlist[2] =', my2dlist[2])            # access the third sublist
print('my2dlist[:][2] =', my2dlist[:][2])      # can't access third element of each sublist
# print('my2dlist[:,2] =', my2dlist[:,2])      # invalid way to access sublist, will cause syntax error

my2darr = np.array(my2dlist)
print('\nmy2darr =\n', my2darr)

print('my2darr[2][:] =', my2darr[2][:])      # access the third row
print('my2darr[2,:] =', my2darr[2,:])        # access the third row
print('my2darr[:][2] =', my2darr[:][2])      # access the third row (similar to 2d list)
print('my2darr[:,2] =', my2darr[:,2])        # access the third column
print('my2darr[:2,2:] =\n', my2darr[:2,2:])     # access the first two rows & last two columns

my2darr = np.arange(1,13,1).reshape(3,4)
print('my2darr =\n', my2darr)

divBy3 = my2darr[my2darr % 3 == 0]
print('\nmy2darr[my2darr % 3 == 0] =', divBy3)            # returns all the elements divisible by 3 in an ndarray

divBy3LastRow = my2darr[2:, my2darr[2,:] % 3 == 0]
print('my2darr[2:, my2darr[2,:] % 3 == 0] =', divBy3LastRow)    # returns elements in the last row divisible by 3



from pandas import Series

s = Series([3.1, 2.4, -1.7, 0.2, -2.9, 4.5])   # creating a series from a list
print('Series, s =\n', s, '\n')

print('s.values =', s.values)     # display values of the Series
print('s.index =', s.index)       # display indices of the Series
print('s.dtype =', s.dtype)       # display the element type of the Series


# Dataframe
from pandas import DataFrame

cars = {'make': ['Ford', 'Honda', 'Toyota', 'Tesla'],
       'model': ['Taurus', 'Accord', 'Camry', 'Model S'],
       'MSRP': [27595, 23570, 23495, 68000]}          
carData = DataFrame(cars)            # creating DataFrame from dictionary
carData                              # display the table


# Basic plotting

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

