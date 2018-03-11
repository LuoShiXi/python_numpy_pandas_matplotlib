##pandas之设置值
import pandas as pd
import numpy as np

dates = pd.date_range('20170101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns = ['A','B','C','D'])

#df.iloc[2,2] = 1111
#print(df)

#df.loc['20170101','B'] = 2222
#print(df)

#df.B[df.A>4] = 0
#print(df)

df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index = \
                    pd.date_range('20170101',periods=6))
print(df)
