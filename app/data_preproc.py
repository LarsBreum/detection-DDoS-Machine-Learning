import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime


udp = pd.read_csv('./data/UDP.csv', low_memory=False)
udp = udp[udp[' Label'].isin(["UDP"])]
udp_cols = list(udp.columns.values)

udp2 = pd.read_csv('./data/DrDoS_UDP.csv', low_memory=False)
udp2 = udp2[udp2['Label'].isin(["DrDoS_UDP"])]
udp2_cols = list(udp.columns.values)

print("---- SHAPES ----")
min = min(udp.shape,udp2.shape)
print("min =", min)
print("----- 7 CLASSES -----")

udp = udp.iloc[:min[0],]
#d.to_csv('./7_classes/udp7.csv')
udp2 = udp2.iloc[:min[0],]
#i.to_csv('./7_classes/udp2.csv')

# Working with 7 classes
print("----- Reading 7_classes -----")

# udp = pd.read_csv("./7_classes/udp7.csv")
# udp2 = pd.read_csv("./7_classes/udp2.csv")

#checking for missing values
udp.isnull().sum()
udp2.isnull().sum()

udp[' Destination IP'] = udp[' Destination IP'].fillna(0)
udp2[' Destination IP'] = udp2[' Destination IP'].fillna(0)
benign_df[' Destination IP'] = benign_df[' Destination IP'].fillna(0)

udp[' Source IP'] = udp[' Source IP'].fillna(0)
udp2[' Source IP'] = udp2[' Source IP'].fillna(0)
benign_df[' Source IP'] = benign_df[' Source IP'].fillna(0)

df = pd.concat([udp, udp2])

print(df.info())

print("---- WORKING WITH ENTIRE DATASET -----")

print("columns: ", len(df.columns))


print(df.columns)
print("df.describe()")
print(df.describe())

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

#removing columns where variation(std) is 0
benign_df=benign_df.drop(' Bwd PSH Flags',axis=1)
benign_df=benign_df.drop(' Fwd URG Flags',axis=1)
benign_df=benign_df.drop(' Bwd URG Flags',axis=1)
benign_df=benign_df.drop('FIN Flag Count',axis=1)
benign_df=benign_df.drop(' PSH Flag Count',axis=1)
benign_df=benign_df.drop(' ECE Flag Count',axis=1)
benign_df=benign_df.drop('Fwd Avg Bytes/Bulk',axis=1)
benign_df=benign_df.drop(' Fwd Avg Packets/Bulk',axis=1)
benign_df=benign_df.drop(' Fwd Avg Bulk Rate',axis=1)
benign_df=benign_df.drop(' Bwd Avg Bytes/Bulk',axis=1)
benign_df=benign_df.drop(' Bwd Avg Packets/Bulk',axis=1)
benign_df=benign_df.drop('Bwd Avg Bulk Rate',axis=1)
benign_df=benign_df.drop('Unnamed: 0',axis=1)
#dfbenign_=df.drop('Unnamed: 0.1',axis=1)
benign_df=benign_df.drop('SimillarHTTP', axis=1)
benign_df=benign_df.drop('Flow ID', axis=1)
#df=df.drop(' Timestamp', axis=1)

df['Label'] = df['Label'].replace('UDP', '1')
df['Label'] = df['Label'].replace('DrDoS_UDP', '1')

benign_df['Label'] = benign_df[' Label'].replace('BENIGN', '0')

#df['Label'] = df[' Label'].astype('int')
print("UNIQUE LABELS: ")
print(df.Label.unique())
print(benign_df.Label.unique())

print("Print label value counts:")
print(df.Label.value_counts())
print(benign_df.Label.value_counts())


print('num = ',len(df[' Source IP'].unique()))
df[' Source IP'].unique()
le = LabelEncoder()
a = df

import netaddr

def convert_ips(column_name, dataframe):
  ips = dataframe[column_name].unique()
  l = len(ips)
  print('starting loop, length is',l)
  for i in range(l):
    dataframe[column_name] = dataframe[column_name].replace(ips[i], int(netaddr.IPAddress(ips[i])))
  print("loop over")
  return dataframe
  


#replacing ip in df with its decimal form
df = convert_ips(' Source IP', df)
df = convert_ips(' Destination IP', df)

benign_df = convert_ips(' Source IP', benign_df)
benign_df = convert_ips(' Destination IP', benign_df)

df['Flow Bytes/s'] = df['Flow Bytes/s'].astype('float')
benign_df['Flow Bytes/s'] = benign_df['Flow Bytes/s'].astype('float')


print("---- HANDLING TIMESTAMPS -----")
print("len timestamps: " + str(len(df[' Timestamp'])))
print(df.head())

df['Timestamp'] = df[' Timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timestamp())
benign_df['Timestamp'] = benign_df[' Timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f").timestamp())


df=df.drop(' Timestamp',axis=1)
benign_df=benign_df.drop(' Timestamp',axis=1)

print("FINAL DF:")
print("head")
print(df.head())


print("describe df")
print(df.describe())


df.to_csv('./out_data/malic_dataset.csv')
