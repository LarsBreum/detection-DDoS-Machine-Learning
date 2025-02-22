import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import netaddr
import sys
import glob
import os

# This file is to take all of the preprocessed data files, make sure that they have the same omount of columns and drop the difference.
# Then, concat the files into one giant .csv which can be used to train a ML model


# TODO: Figure out which columns I want and drop the ones I don't want. Go through all of the files in chunks and concat them together.

# Get a list of all CSV files in the directory
filenames = glob.glob("./out_data/*.csv")
df_columns = []
first_chunk = True

for file in filenames:
    df_columns.append(pd.read_csv(f'./{file}',  nrows = 0))

common_columns = set.intersection(*df_columns)
print(common_columns)

# Now I need to go through all files in chunks, remove the unneeded columns and append to the same file.
for file in filenames:
    for df in pd.read_csv(f'./{file}',low_memory = False, chunksize = 100000):
        df = df[common_columns]
        print(df.head())

        df.astype({"Label": int})
        df = df.dropna(subset=['Label'])

        if first_chunk:
            df.to_csv(f'./out_data/complete_processed.csv', index=False, mode='a', header=True)
            first_chunk = False
        else:
            df.to_csv(f'./out_data/complete_processed.csv', index=False, mode='a', header=False)
    



# UDP_columns = pd.read_csv('./out_data/UDP.csv',  nrows = 0)

# df_UDP = pd.read_csv('./out_data/UDP.csv', on_bad_lines='skip')
# df_UDP.columns = df_UDP.columns.str.strip()

# df_benign = pd.read_csv('./out_data/BENIGN.csv', on_bad_lines='skip', low_memory=False)
# df_benign.columns = df_benign.columns.str.strip()

# common_columns = df_UDP.columns.intersection(df_benign.columns)
# df_benign = df_benign[common_columns]
# df_benign.drop(df_benign[df_benign['Label'] != 0].index, inplace=True)

# df_UDP = df_UDP[common_columns]
# df_UDP.drop(df_UDP[df_UDP['Label'] != 1].index, inplace=True)

# df_benign.to_csv('./out_data/BENIGN_processed.csv')
# df_UDP.to_csv('./out_data/UDP_processed.csv')

# df_complete = pd.concat([df_benign, df_UDP])
# print(df_complete["Label"].unique)
# print(df_complete.isna().sum())

# df_complete = df_complete.dropna(subset=['Label'])

# print("NaN:")
# print(df_complete["Label"].unique)
# print(df_complete.isna().sum())

# df_complete = df_complete.astype({"Label": int})
# df_complete.to_csv("./out_data/complete_processed.csv")
