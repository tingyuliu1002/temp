import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

file = r'G:\TFG\ML\data\percentage.xlsx'

df1 = pd.read_excel(file, engine='openpyxl',usecols = [1,2,3,4,5,6])
df1 = df1.loc[0].values
df1 = np.array(df1)
df2 = pd.read_excel(file, engine='openpyxl',usecols=[1,2,3,4,5,6])
df2 = df2.loc[1].values
df2 = np.array(df2)
df3 = pd.read_excel(file, engine='openpyxl',usecols=[1,2,3,4,5,6])
df3 = df3.loc[2].values
df3 = np.array(df3)
df4 = pd.read_excel(file, engine='openpyxl',usecols=[1,2,3,4,5,6])
df4 = df4.loc[3].values
df4 = np.array(df4)
times = [0,1,3,5,10,15]
times = np.array(times)


x1 = np.arange(0,15,0.1)
func = interpolate.interp1d(times,df1,kind='cubic')
y1= func(x1)
x2 = np.arange(0,15,0.01)
func = interpolate.interp1d(times,df2,kind='cubic')
y2= func(x2)
x3 = np.arange(0,15,0.01)
func = interpolate.interp1d(times,df3,kind='cubic')
y3= func(x3)
x4 = np.arange(0,15,0.1)
func = interpolate.interp1d(times,df4,kind='cubic')
y4= func(x4)



plt.title("Result",fontdict={'size': 20})
plt.xlabel("time(min)",fontdict={'size': 20})
plt.ylabel("RecA bind(%)",fontdict={'size': 20})
plt.xlim(0,16)
plt.ylim(0,100)
plt.plot(times,df1,color='darkgrey',label='ATPgs', markersize="8",marker = 'o')
plt.plot(times,df2,color='cadetblue',label='ATP', markersize="8",marker = 'o')
plt.plot(times,df3,color='darkorange',label='cdiAMP', markersize="8",marker = 'o')
plt.plot(times,df4,color='gold',label='cdiGMP', markersize="8",marker = 'o')
plt.legend()
#plt.text(x1[2], y1[2],'74')



plt.show()




