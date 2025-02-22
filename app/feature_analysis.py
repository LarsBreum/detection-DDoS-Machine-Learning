import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import netaddr
import sys
import glob
import os


for df in pd.read_csv(f'./out_data/complete_processed.csv',low_memory = False, chunksize = 1000000):
    pd.set_option('display.max_columns', None)

    print("NaN:")
    print(df.isna().sum())
    print("DESCRIBE:")
    print(df.describe())