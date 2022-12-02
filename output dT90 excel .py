import openpyxl as xl
import pandas as pd
import os
from basic.select import select_file,select_folder

df1 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-1 done')
df2 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-2 done')
df3 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('2-1 done')
df4 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('2-2 done')
df5 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('3-1 done')
df6 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('3-2 done')
df7 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('4-1 done')
df8 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('4-2 done')
df9 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('4-2 done')
dfA = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9])



# 開一個新的excel並把多個df寫到同excel不同sheet
dir = r'G:\TFG\20220128\dT90.xlsx'
writer = pd.ExcelWriter(dir, engine='openpyxl') # 指定引擎openpyxl

dfA.to_excel(writer) # 存到指定的sheet


writer.save() # 存檔生成excel檔案





