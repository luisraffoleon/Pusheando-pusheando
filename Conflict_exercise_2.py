arr = np.array([1,2,3,4])

index_array = np.array([arr[0],arr[3]])

print(index_array)

#A.2 Get the third and fourth element fomr the following array and add them. 

arr = np.array([1,2,3,4])

print(arr[2]+ arr[3])

# How to acces a 2-D Array 

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

# How to access a 3-D Array: 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

arr[0, 1, 2] prints the value 6.

#And this is why:

#The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
#Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

#The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
#Since we selected 1, we are left with the second array:
[4, 5, 6]

#The third number represents the third dimension, which contains three values:
4
5
6
#Since we selected 2, we end up with the third value:
6

#Negative Indexing: 

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])