import pandas as pd
from basic.select import select_file, select_folder
import os

path1 = select_file()
path2 = select_file()
path3 = select_file()
path4 = select_file()
path5 = select_file()

path  =  select_folder()
p1 = os.path.join(path, "0.glimpse")
p2 = os.path.join(path, "1.glimpse")

p3 = os.path.join(path, "header.glimpse")
p4 = os.path.join(path, "header.txt")
p5 = os.path.join(path, "header-time.txt")



os.rename(path1, p1)
os.rename(path2, p2)
os.rename(path3, p3)
os.rename(path4, p4)
os.rename(path5, p5)

