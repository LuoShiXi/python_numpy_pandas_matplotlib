#numpy-分割split

import numpy as np

A = np.arange(12).reshape((3,4))
print(A)

print(np.split(A,2,axis=1))
#axis=1为横向(按行 为索引)分割为列数组，参数2表示总共4列进行等量两列分割，分割为2个array

##print(np.split(A,3,axis=1))#会报错，因为4列无法33分

##不等量分割，例如：4列分成3个数组2列、1列、1列
print(np.array_split(A,3,axis=1))

###重要！！！
#vsplit splits along the vertical axis, and array_split allows one to specify along which axis to split.
#vsplit沿垂直轴分割，array_split允许沿着任意哪个轴指定分割。

print(np.vsplit(A,3))
#vsplit相当于axis = 0（默认）分割，数组总是沿第一个轴分割，而不管数组的维度如何。
print(np.hsplit(A,2))
#hsplit is equivalent to split with axis=1,
#the array is always split along the second axis regardless of the array dimension.




