#Locality of Reference
#In computer science, locality of reference, also known as the principle of locality
#There are two basic types of reference locality – temporal and spatial locality. 
#Temporal locality refers to the reuse of specific data, and/or resources, within a relatively small time duration. 
#Spatial locality (also termed data locality[3]) refers to the use of data elements within relatively close storage locations. Sequential locality, a special case of spatial locality, occurs when data elements are arranged and accessed linearly, such as, traversing the elements in a one-dimensional array. 

#NumPy stands for Numerical Python.
#NumPy is a python library used for working with arrays.
#In Python we have lists that serve the purpose of arrays, but they are slow to process.
#NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
#The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
#NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
#NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray.

import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
print(c)
toc = time.time()

print("Vectorised version: " + str(1000*(toc-tic)) + " ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print(c)
print("For loop: " + str(1000*(toc-tic)) + " ms")

arr = np.array(42)
print(arr)
print(arr.ndim)
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)
print(type(arr))
