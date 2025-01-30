import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import netaddr

filenames = ('UDPLag.csv','LDAP.csv', 'NetBIOS.csv', 'Portmap.csv', 'Syn.csv', 'TFTP.csv')

def convert_ips(column_name, dataframe):
  ips = dataframe[column_name].unique()
  l = len(ips)
  print('starting loop, length is',l)
  for i in range(l):
    dataframe[column_name] = dataframe[column_name].replace(ips[i], int(netaddr.IPAddress(ips[i])))
  print("loop over")
  return dataframe

def process_benign(df):
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

    df['Label'] = df[' Label'].replace('BENIGN', '0')

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
    df.to_csv(f'./out_data/benign_{file}.csv')



for file in filenames:
    print(f"Loading in file: {file}")
    df = pd.read_csv(f'./data/{file}', low_memory=False)
    df = df[df[' Label'] == 'BENIGN']
    df.to_csv(f'./data/benign_{file}')
    print(f"Outputted benign data for: {file}")
    print(f"processing data for: {file}")
    process_benign(df)
    print(f"Processed: {file}")
    del(df)



print("Done with extracting benign data")