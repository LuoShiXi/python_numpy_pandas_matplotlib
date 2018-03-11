import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])


# vertical stack 垂直组合
##print(np.vstack((A,B)))

##C = np.vstack((A,B))
##
##print(A.shape) #A可以看作一维数组，shape为（3，）
##print(C.shape) #C可以看作二维数组，shape为（2，3），
#第一个参数为第一维的长度，第二个参数为第二维的长度


# horizontal stack 水平合并
##D = np.hstack((A,B))
##print(D)
##print(A.shape,D.shape)


print(A.shape)
print(A.T) #无法将A由一行变为一列
print(A[:,np.newaxis]) #将横向的[1,1,1]变为竖向

'''
    另一种横向变竖向的方式为：
'''
Q = np.array([1,1,1])[:,np.newaxis]
print(Q)

'''
另另外一种横向组合方式：
'''
print(A)
print(B)
P = np.concatenate([A,Q],axis=0)
#再补充：只能合并矩阵或者维度相同的列向量或者合并一维行向量
#补充：合并时两个矩阵向量必须具有相同的维度(行列相同)
#axis表示为numpy中数组的轴，改变0、1的值，即改变行列的指示
#在numpy中，axis=0表示纵向合并、axis=1表示横向合并
#！！！注意：当array为一维的行向量时，
#axis=0输出的为横向合并结果，当axis=1时无法进行，语句错误WHY???
print(P)

























