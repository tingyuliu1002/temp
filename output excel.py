import openpyxl as xl
import pandas as pd
import os
from basic.select import select_file,select_folder

#1
df11 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-1 done')
df12 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-2 done')
df13 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-3 done')
#df14 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
#print('1-4 done')
dft1 = pd.concat([df11,df12,df13])

#3
df31 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-1 done')
df32 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-2 done')
df33 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('1-3 done')
#df14 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
#print('1-4 done')
dft1 = pd.concat([df11,df12,df13])

#5
df51 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('5-1 done')
df52 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('5-2 done')
df53 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('5-3 done')
#df54 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
#print('5-4 done')
dft5 = pd.concat([df51,df52,df53])



#10
df101 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('10-1 done')
df102 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('10-2 done')
df103 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('10-3 done')
#df104 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
#print('10-4 done')
dft10 = pd.concat([df101,df102,df103])



#15
df151 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('15-1 done')
df152 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('15-2 done')
df153 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
print('15-3 done')
#df154 = pd.read_excel (select_file(), sheet_name='med_attrs',usecols=[1])
#print('15-4 done')
dft15 = pd.concat([df151,df152,df153])

# 開一個新的excel並把多個df寫到同excel不同sheet
dir = r'G:\TFG\20220127\snapshots\1A3T.xlsx' # 設定路徑及檔名
writer = pd.ExcelWriter(dir, engine='openpyxl') # 指定引擎openpyxl

dft1.to_excel(writer, sheet_name='1') # 存到指定的sheet
dft5.to_excel(writer, sheet_name='5') # 存到指定的sheet
dft10.to_excel(writer, sheet_name='10') # 存到指定的sheet
dft15.to_excel(writer, sheet_name='15') # 存到指定的sheet
writer.save() # 存檔生成excel檔案





