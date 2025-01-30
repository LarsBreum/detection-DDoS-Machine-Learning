import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

import netaddr

def convert_ips(column_name, dataframe):
  ips = dataframe[column_name].unique()
  l = len(ips)
  print('starting loop, length is',l)
  for i in range(l):
    dataframe[column_name] = dataframe[column_name].replace(ips[i], int(netaddr.IPAddress(ips[i])))
  print("loop over")
  return dataframe

filenames = {'UDP', 'DrDoS_UDP'}

for file in filenames:
  print(f"loading in file: {file}.csv")
  df = pd.read_csv(f'./data/{file}.csv', low_memory=False)
  df = df[df[' Label'] == file]  # Keep only rows where A >= 30

  df[' Destination IP'] = df[' Destination IP'].fillna(0)
  df[' Source IP'] = df[' Source IP'].fillna(0)
  print(df.info())
  #removing columns where variation(std) is 0
  df=df.drop(' Bwd PSH Flags',axis=1)
  df=df.drop(' Fwd URG Flags',axis=1)
  df=df.drop(' Bwd URG Flags',axis=1)
  df=df.drop('FIN Flag Count',axis=1)
  df=df.drop(' PSH Flag Count',axis=1)
  df=df.drop(' ECE Flag Count',axis=1)
  df=df.drop('Fwd Avg Bytes/Bulk',axis=1)
  df=df.drop(' Fwd Avg Packets/Bulk',axis=1)
  df=df.drop(' Fwd Avg Bulk Rate',axis=1)
  df=df.drop(' Bwd Avg Bytes/Bulk',axis=1)
  df=df.drop(' Bwd Avg Packets/Bulk',axis=1)
  df=df.drop('Bwd Avg Bulk Rate',axis=1)
  df=df.drop('Unnamed: 0',axis=1)
  #df=df.drop('Unnamed: 0.1',axis=1)
  df=df.drop('SimillarHTTP', axis=1)
  df=df.drop('Flow ID', axis=1)
  #df=df.drop(' Timestamp', axis=1)

  df['Label'] = df[' Label'].replace(file, '1')
  df['Label'] = df[' Label'].replace(file, '1')

  #replacing ip in df with its decimal form
  df = convert_ips(' Source IP', df)
  df = convert_ips(' Destination IP', df)

  df['Flow Bytes/s'] = df['Flow Bytes/s'].astype('float')


  print("---- HANDLING TIMESTAMPS -----")
  print("len timestamps: " + str(len(df[' Timestamp'])))
  print(df.head())

  df['Timestamp'] = df[' Timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timestamp())


  df=df.drop(' Timestamp',axis=1)
  print(df.describe())
  df.to_csv(f'./out_data/{file}_malic_dataset.csv')
  del(df)


