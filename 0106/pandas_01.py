import pandas as pd
import numpy as np

#Series序列，输出带有index索引
s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20170106',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),\
                  index = dates,columns = ['a','b','c','d'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

df2 = pd.DataFrame({'A':123,\
                    'B':pd.Categorical(["aa","bb"])})
print(df2)

print(df2.dtypes)
print(df2.index.sort_values(return_indexer=True,ascending=False))

print(df2.describe())

print(df2.T)


print(df2.sort_index(axis=0,ascending=False))
#在pandas中，axis=1代表的是纵轴列标
#ascending=False为倒序，True为正序

print(df2.sort_values('B',ascending=True))#按某一索引排序

























