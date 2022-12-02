import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import openpyxl


file = r'G:\TFG\20220411\over 70.xlsx'   #filename
graph_title = 'ATP 1min'
dir = os.path.join(r'G:\TFG\20220411\graph\over 70', graph_title) #savefig

nt = pd.read_excel(file,usecols=[0],skiprows =0,nrows=3)
per = pd.read_excel(file,usecols=[1],skiprows =0,nrows=3)
nt = nt.T
per = per.T
nt = nt.values.tolist()
per = per.values.tolist()
nt = np.ravel(nt)
per = np.ravel(per)
print(nt)
print(per)

plt.bar(nt, per,width = 0.5, color='#B6D8FA', edgecolor='#FFFFFF')
plt.xticks(fontsize=12)
plt.xlabel('Nucleotide',fontsize=14)
plt.ylabel('Over 70nm Percentage (%)',fontsize=14)
plt.title('ATP over 70nm Percentage',fontsize=18)
plt.ylim(0,100)
plt.savefig(dir)
plt.show()



