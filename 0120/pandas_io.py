import pandas as pd

file = 'F:\\py3.6_workspace\\0120\\student.csv'
data = pd.read_csv(file)
print(data)

data.to_pickle('student.pickle')
