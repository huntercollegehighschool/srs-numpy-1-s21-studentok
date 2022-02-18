# 1. Import the numpy package under the name `np`
import numpy as np

##### DECLARING NUMPY ARRAYS #####

# 2. Use np.array(<list>) to convert the list below into a numpy array. The array should be saved in a variable. Then print both the list and the array.
a = [300, -200, 100, 0, -100, 200, -300]
array_a = np.array(a)

print(a)
print(array_a)

## The array method in numpy has an optional dtype argument which specifies the datatype each element should be. For the array above, it could be implemented using A = np.array(a, dtype=str) ##

# 3. Declare new arrays with different datatypes using the list from #2. Datatypes to use: str, float, np.int32, np.int8, np.uint32, up.uint8.
array_str = np.array(a,dtype=str)
array_float = np.array(a,dtype=float)
array_int32 = np.array(a,dtype=np.int32)
array_int8 = np.array(a,dtype=np.int8)
array_uint32 = np.array(a,dtype=np.uint32)
array_uint8 = np.array(a,dtype=np.uint8)
print(array_str)
print(array_float)
print(array_int32)
print(array_int8)
print(array_uint32)
print(array_uint8)

# 4. Use np.zeros(<int>) to create a array of zeroes of size 10. This should be saved in a variable. Then print the array.
array_y = np.zeros(10)
print(array_y)

# 5. In your array of zeroes, change the fifth 0 to a 6. (remember how indexing works in lists?) Print the array.
array_y[4] = 6
print(array_y)

# 6. Use np.arange(<int>, <int>) to create an array with values ranging from 11 to 46. Print the array.
array_z = np.arange(11,47) 
print(array_z)


# 7. Reverse the array you created in #6. Print the array.
array_inv = array_z[::-1]
print(array_inv)

# 8. Use <array>.reshape(<int>, <int>) to turn your array from #6 into a multidimensional 6x6 array. Print the array.
multi_array = array_z.reshape(6,6)
print(multi_array)


# 9. Use np.random.random((<int>, <int>)) to create a 10x10 array with random values. Print the array.
random_array = np.random.random((10,10))
print(random_array)


# 10. Use np.random.randint(<int>, <int>, size=(<int>, <int>)) to create a 3x3 array with random integers. Print the array.
random_array_II = np.random.randint(0,100,size=(3,3))
print(random_array_II)

# 11. Use <array>.max() and <array>.min to identify the maximums and minimums of the arrays you created in #9 and #10. Print the results.
maximal = random_array.max()
maximal_2 = random_array_II.max()
minimal = random_array.min()
minimal_2 = random_array_II.min()
print(maximal, maximal_2, minimal, minimal_2)

# 12. Use <array>.mean() to find the means of the two arrays you created in #9 and #10. Print the results.
mean = random_array.mean()
meaner = random_array_II.mean()
print(mean,meaner)

# 13. Convert the following two lists into 2X3 arrays. (You will need to use np.array and .reshape)

a = [2, 3, 5, 7, 11, 13]
b = [3, 1, 4, 1, 5, 9]

array_1 = np.array(a) 
array_1 = array_1.reshape(2,3)
print(array_1)
array_2 = np.array(b)
array_2 = array_2.reshape(2,3)
print(array_2)
# 14. Add the two arrays from #13 (<array> + <array>)
array_3 = array_1 + array_2
print(array_3)

# 15. Multiply both arrays from #13 by 10.

array_10 = array_1*10
array_20 = array_2*10
print(array_10)
print(array_20)