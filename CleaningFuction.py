import numpy as np
import pandas as pd
import echarts as ech
import os




#


#


# Dir where all the datasets are stored
data_dir = r"D:\Downloads\Stackoverflow_Data _2011_to_2020\all"

# iterate through the folder to read the data into corresponding dataframes,
# files is the list to store all the file names:
files = []

for r, d, f in os.walk(data_dir): # r=root, d=directories, f = files
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
print(files)

# read CSV function reads the CSV file and perform initial data wrangling on the file.








#
