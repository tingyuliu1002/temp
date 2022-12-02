import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from basic.select import select_file, select_folder
import pandas as pd
import os
# import function
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

bin_size = 4
bin_number = 120 / bin_size
bin_number = int(bin_number)
sheetname = '60' #snapshot's minute
graph_title  = sheetname + 'min' #sheetname + 'min'

name = 'ATPrs1'   #filename
filename = os.path.join(r'G:\TFG\20220425', name +'.xlsx')   #run file
dir = os.path.join(r'G:\TFG\20220425\graph', name + graph_title)   #savefig
data1_mean_new = 36.6
data1_std_new = 6

df = pd.read_excel(filename, engine='openpyxl',sheet_name=sheetname,usecols = [0])
data_original = np.array(df)
data = []
for i in data_original:
    if(i > 0 and i < 120):
        data.append(float(i))
    n = 0
    for j in data:
        if (j > data1_mean_new + data1_std_new):
            n = n + 1
percentage = int(n / (len(df) + 1) * 100)
# percentage = str(percentage) + '%'
data.sort()
data_mean = np.mean(data)
print(percentage)
data_std = np.std(data, ddof=1)

data_mean_new = np.mean(data)
data_std_new = np.std(data, ddof=1)
m = len(data)
bounds = ((0,0,0),(m*2, data_mean_new*3, data_std_new*3))
count ,edges = np.histogram(data, bin_number)
center = []
edges = list(edges)
for i in range(len(edges)-1):
  center += [(edges[i] + edges[i+1])/2]
weights = np.ones_like(data) / float(len(data))



mean_str = str(round(data_mean,2))

plt.xlim(0,120)
plt.ylim(0,0.4)
plt.vlines(x=data_mean, ymin=0, ymax=0.4,colors='r',linestyles='--')
plt.axvspan(data1_mean_new - data1_std_new, data1_mean_new + data1_std_new, color='silver', alpha=0.5, lw=0)
if (name == 'cdiA') or (name == '3A1T') or(name == '2A2T') or (name == '1A3T'):
    plt.axvspan(0, data1_mean_new - data1_std_new, color='lightcyan', alpha=0.5, lw=0)
#plt.text(75,0.3,'mean = ' + mean_str + '(nm)',fontsize=11,horizontalalignment='left')
plt.text(75,0.32,str(percentage) +'%',fontsize=25,horizontalalignment='left',color='grey')
plt.title(graph_title,fontsize=22, fontname='Times')
plt.hist(data, bin_number, range=(0, 150), weights=weights, color='#B6D8FA', edgecolor='#FFFFFF')
plt.xlabel('Brownian Motion (nm)', fontsize=16, fontname='Times')
plt.ylabel('Possibility', fontsize=16, fontname='Times')
plt.savefig(dir)




