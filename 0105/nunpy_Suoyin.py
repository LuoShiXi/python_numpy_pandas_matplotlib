import numpy as np

'''
A = np.arange(3,15)#.reshape((3,4))
print(A)
print(A[3])



print(A[1]) #此时A[1]表示为二维空间里第二行，以整行为元素

print(A[1][1])#第一行第一列(行列从零开始)
print(A[1,1])#同上

print(A[1,1:3])#第一行的第一列到第二列

print(A[1:3,2])
'''

A = np.arange(3,15).reshape((3,4))
print(A)

for row in A:
    print(row)

for column in A.T:
    print(column)

print(A.flatten())
#flat属性将返回一个flatiter对象，可以遍历多维数组或者遍历矩阵
for item in A.flat:
    print(item)















