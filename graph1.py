import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from basic.select import select_file, select_folder
import pandas as pd
import os

bin_size = 5
bin_number = 120 / bin_size
bin_number = int(bin_number)
sheetname = "5"    #snapshot's minute
graph_title  = sheetname + 'min'


filename = r'G:\TFG\20211229\1r3x\1r3x.xlsx'
dir=r'G:\TFG\20211229\1r3x'
#filename = RecA
#dir = savefig


df = pd.read_excel(filename, engine='openpyxl',sheet_name=sheetname,usecols = [1])
data_original = np.array(df)
data = []
for i in data_original:
    if(i > 0 and i<120):
        data.append(float(i))
data.sort()
data_mean = np.mean(data)
print(data_mean)
data_std = np.std(data, ddof=1)

data1_mean_new = 44
data1_std_new = 5

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

plt.xlim(0,120)
plt.ylim(0,0.2)
plt.axvspan(data1_mean_new - data1_std_new, data1_mean_new + data1_std_new, color='silver', alpha=0.5, lw=0)
plt.title(graph_title,fontsize=22, fontname='Times')
plt.hist(data, bin_number, range=(0, 150), weights=weights, color='#B6D8FA', edgecolor='#FFFFFF')
plt.xlabel('Brownian Motion (nm)', fontsize=16, fontname='Times')
plt.ylabel('Possibility', fontsize=16, fontname='Times')
#plt.savefig(dir)


