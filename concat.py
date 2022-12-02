import openpyxl as xl
import pandas as pd
import os
from basic.select import select_file,select_folder


df1 = pd.read_excel(select_file(),usecols=[1])
df2 = pd.read_excel(select_file(),usecols=[1])
df3 = pd.read_excel(select_file(),usecols=[1])
df4 = pd.read_excel(select_file(),usecols=[1])
dfA = pd.concat([df1, df2, df3, df4])

dir = select_folder()
name = 'ATPgs.xlsx'
path = os.path.join(dir + name)
writer = pd.ExcelWriter(path, engine='openpyxl')

dfA.to_excel(writer) # 存到指定的sheet
writer.save()
