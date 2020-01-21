from os import getcwd, listdir
import numpy as np
import pandas as pd

data_path = getcwd() + "/data"
df_dict = {i[:-4]: pd.read_csv(f"{data_path}/{i}") for i in listdir(data_path)}

union_df = df_dict['M191_student_data'][df_dict['M191_student_data']['Student Name'].isin(df_dict['M196_student_data']['Student Name']) == True]

union_df['Student Name'].shape
