import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import netaddr
import sys
import glob
import os

def convert_ips(column_name, dataframe):
  ips = dataframe[column_name].unique()
  l = len(ips)
  print('starting loop, length is',l)
  for i in range(l):
    dataframe[column_name] = dataframe[column_name].replace(ips[i], int(netaddr.IPAddress(ips[i])))
  print("loop over")
  return dataframe

def process(df, label = "BENIGN", label_value = 0):
    df[' Destination IP'] = df[' Destination IP'].fillna(0)
    df[' Source IP'] = df[' Source IP'].fillna(0)

    print(df.info())

    #removing columns where variation(std) is 0
    df = df.drop(columns=df.select_dtypes(include=np.number).loc[:, lambda x: x.std() <= 0.1].columns)
    print("Desribe numbers")

    # Compute standard deviation for numeric columns
    std_values = df.select_dtypes(include=np.number).std()

    # Print column names and their standard deviation
    for col, std in std_values.items():
        print(f"Column: {col}, Standard Deviation: {std}")

    df['Label'] = df[' Label'].replace(label, label_value) #replace label with a numeric value

    print('num = ',len(df[' Source IP'].unique()))
    df[' Source IP'].unique()
    le = LabelEncoder()
    a = df

    
    #replacing ip in df with its decimal form
    df = convert_ips(' Source IP', df)
    df = convert_ips(' Destination IP', df)
    df['Flow Bytes/s'] = df['Flow Bytes/s'].astype('float')
    print("---- HANDLING TIMESTAMPS -----")
    print("len timestamps: " + str(len(df[' Timestamp'])))
    print(df.head())

    df['Timestamp'] = df[' Timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timestamp())
    df=df.drop(' Timestamp',axis=1)
    print("describe df")
    print(df.describe())
    print(f"Writing: ./out_data/{out_file}.csv")
    df.to_csv(f'./out_data/{label}.csv', index=False, mode='a', header=False)


if len(sys.argv) < 3:
  print("Please provide three arguments. LABEL, chunksize and label_value.")
else:

  chunk = sys.argv[2]

  # Get a list of all CSV files in the directory
  filenames = glob.glob("./data/*.csv")
  print(f"Extracting label: {sys.argv[1]}")
  print(f"Labeling with the value: {sys.argv[3]}")

  
  out_file = sys.argv[1]

  for file in filenames:
    print(f"Loading in file: {file}")
    for df in pd.read_csv(f'./{file}',low_memory = False, chunksize = int(chunk)):
      print(f"Processing chunk with {len(chunk)} rows")

      df = df[df[' Label'] == sys.argv[1]]

      if df.empty:
        print("No data in this chunk. Carry on.")
        continue
        
      print(f"Outputted {sys.argv[1]} data for: {file}")
      print(f"processing data for: {file}")
      process(df, f"{sys.argv[1]}", sys.argv[3])
      print(f"Processed: {file}")
      del(df)


print(f"Done {sys.argv[1]} data")



