#pandas学习之选择数据
import pandas as pd
import numpy as np

dates = pd.date_range('20170119',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),
                  index=dates,
                  columns=['A','B','C','D'])
print(df)

#print(df.A,df['A'])
#print(df[0:3],df['20170120':'20170122'])

##select by label标签:local
#print(df.loc['20170120'])
#print(df.loc[:,['A','B']])
#print(df.loc['20170122',['A','B']])

##select by position序列:iloc
#print(df.iloc[3])#第3行，从0开始
#print(df.iloc[3:5,1:3])
#print(df.iloc[[1,3,5],1:3])

##mixed selection:ix混合
#print(df.ix[:3,['A','B']])

##Boolean indexing
print(df.A)
print(df[df.A>8])











