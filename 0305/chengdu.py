import pandas as pd

file = "F:\\py3.6_workspace\\0201_txt\\20140804__09_89h_01.csv"

data = pd.read_csv(file)
li = open(file,'r')
lines = li.readlines()
two_circle = open('./two_circle.csv','w')
two_circle.truncate()
#二环，东西南北，经纬度最小与最大值，以便取二环内数据
lat_min = 30.620901
lat_max = 30.700681
lng_min = 104.019787
lng_max = 104.115858

lat = data.iloc[:,0]
lng = data.iloc[:,1]
j = 0
for i in range(len(lat)):
    if (lat[i]>lat_min) & (lat[i]<lat_max)\
       & (lng[i]>lng_min) & (lng[i]<lng_max):
        #print(lat[i],lng[i])
        #print(lines[i+1])
        #print(str(lat[i]+0.05))
        two_circle.write(str(lat[i]+0.0025)+','+str(lng[i]-0.0025)+'\n')
        j+=1
print(j)
two_circle.close()
li.close()





    

