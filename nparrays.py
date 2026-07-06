import numpy as np 

mylist = [1,2,3]

#print(type(mylist))

myarray = np.array(mylist)

#print(type(myarray))

#print(np.arange(0,10,3))

#print(np.zeros((3,2)))

np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)
print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())
print(arr.mean())
print(arr.reshape(2,5))

arr2 = np.random.randint(0,100,10)
#print(arr2)

print()

mat = np.arange(0,100).reshape((10,10))

print(mat)
print(mat[3,6])
print(mat[:,2]) 
print(mat[:,2].reshape(10,1)) 
print(mat[4,:])
mat[0:4,:] = 42
print(mat)
