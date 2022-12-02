import openpyxl as xl
import pandas as pd
import os
from basic.select import select_file,select_folder

"""
target_path = select_folder()
all_content = os.listdir(target_path)
length = len(all_content)
print('get length')
snapshot_time = length/3
"""
snapshot_time = 6 #snapshots total time counts (e.g. 3, 6, 9 min snapshots -> 3)


i = 1
while i <= snapshot_time:
    df1 = pd.read_excel(select_file(), sheet_name='med_attrs', usecols=[1])
    df2 = pd.read_excel(select_file(), sheet_name='med_attrs', usecols=[1])
    df3 = pd.read_excel(select_file(), sheet_name='med_attrs', usecols=[1])
    df = pd.concat([df1, df2, df3])
    #print(df)
    if i == 1 :
        # 開一個新的excel並把多個df寫到同excel不同sheet
        path = r'G:\TFG\20220425'
        name = 'ATP1-1.xlsx'
        dir = os.path.join(path, name)  # 設定路徑及檔名
        writer = pd.ExcelWriter(dir, engine='openpyxl')  # 指定引擎openpyxl
    df.to_excel(writer, sheet_name = str(i))  # 存到指定的sheet
    i = i + 1


writer.save() # 存檔生成excel檔案