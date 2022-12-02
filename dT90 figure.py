import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from basic.select import select_file, select_folder
import pandas as pd
import os
# import function
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

graph_title  = 'dT90'
dir = os.path.join(select_folder() + '/ ' + graph_title)
bin_number = 30
#first select_folder() = path
#second select_file() = dT90

filename = select_file()
df = pd.read_excel(filename, engine='openpyxl',usecols = [1])
# df = pd.read_excel(filename, engine='openpyxl',sheet_name=sheetname,usecols = ["BMx_sliding"])
data_original = np.array(df)
data = []
for i in data_original:
    if(i > 0 and i<120):
        data.append(float(i))
data.sort()
for i in data:
    print(i)
data_mean = np.mean(data)
print(data_mean)
data_std = np.std(data, ddof=1)
##data = np.array([x for x in data if x<data_mean+10 and x>data_mean-10])
print(np.mean(data))

data_mean_new = np.mean(data)
data_std_new = np.std(data, ddof=1)
m = len(data)
bounds = ((0,0,0),(m*2, data_mean_new*3, data_std_new*3))
count ,edges = np.histogram(data, bin_number)
center = []
edges = list(edges)
for i in range(len(edges)-1):
  center += [(edges[i] + edges[i+1])/2]
x = np.arange(data_mean_new - data_std_new*4, data_mean_new + data_std_new*4, 0.5)
popt, pcov = curve_fit(gauss_function, center, count, p0 = [m/2, data_mean_new, data_std_new], bounds=bounds)
#weights = np.ones_like(data) / float(len(data))

k = str('N = ') + str(len(df)+1)
plt.xlim(0,120)
plt.ylim(0,40)
plt.text(120,180,k,fontsize=18   #新增文字
         ,verticalalignment = "top",horizontalalignment = "right",
         bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
plt.axvspan(data_mean_new - data_std_new, data_mean_new + data_std_new, color='silver', alpha=0.5, lw=0)
plt.title(graph_title,fontsize=22, fontname='Times')
#plt.hist(data, bin_number, weights=weights, color='#B6D8FA', edgecolor='#FFFFFF')
plt.hist(data, bin_number, color='#B6D8FA', edgecolor='#FFFFFF')
plt.plot(x, gauss_function(x, *popt), label='fit', color='#003366')
plt.xlabel('Brownian Motion (nm)', fontsize=16, fontname='Times')
plt.ylabel('Counts', fontsize=16, fontname='Times')
#plt.savefig(dir)


BM_mean = popt[1]
BM_std = popt[2]
print(f'BM of mean is {np.mean(data)}')
print(f'BM of std is {BM_std}')
print(f'bin size is {center[1]-center[0]}')
print(k)