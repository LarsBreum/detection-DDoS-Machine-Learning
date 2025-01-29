import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
 
udp = pd.read_csv('./data/Own_UDP.csv', low_memory=False)
udp = udp[udp['Label'].isin(["UDP"])]

#checking for missing values
udp.isnull().sum()

udp['Dst IP'] = udp['Dst IP'].fillna(0)
udp['Src IP'] = udp['Src IP'].fillna(0)

df = udp

print(df.info())

print("---- WORKING WITH ENTIRE DATASET -----")

print("columns: ", len(df.columns))


print(df.columns)
print("df.describe()")
print(df.describe())

#removing columns where variation(std) is 0
df=df.drop('Bwd PSH Flags',axis=1)
df=df.drop('Fwd URG Flags',axis=1)
df=df.drop('Bwd URG Flags',axis=1)
df=df.drop('FIN Flag Count',axis=1)
df=df.drop('PSH Flag Count',axis=1)
df=df.drop('ECE Flag Count',axis=1)
df=df.drop('Fwd Bytes/Bulk Avg',axis=1)
df=df.drop('Fwd Packet/Bulk Avg',axis=1)
df=df.drop('Fwd Bulk Rate Avg',axis=1)
df=df.drop('Bwd Bytes/Bulk Avg',axis=1)
df=df.drop('Bwd Packet/Bulk Avg',axis=1)
df=df.drop('Bwd Bulk Rate Avg',axis=1)
#df=df.drop('Unnamed: 0',axis=1)
#df=df.drop('Unnamed: 0.1',axis=1)
#df=df.drop('SimillarHTTP', axis=1)
df=df.drop('Flow ID', axis=1)
#df=df.drop('Timestamp', axis=1)

df['Label'] = df['Label'].replace('UDP', '1')


#df['Label'] = df[' Label'].astype('int')
print("UNIQUE LABELS: ")
print(df.Label.unique())

print("Print label value counts:")
print(df.Label.value_counts())

print(df.count())

print('num = ',len(df['Src IP'].unique()))
df['Src IP'].unique()
le = LabelEncoder()
a = df


import netaddr
print(int(netaddr.IPAddress('192.168.4.54')))
ips = df['Dst IP']
converted=[]
for i in range(len(ips)):
  try:
    converted.append(int(netaddr.IPAddress(ips[i])))

  except:
    converted.append(0)

print("done")

#replacing ip in df with its decimal form
ips = df['Src IP'].unique()
l = len(ips)
print('starting loop, length is',l)

for i in range(l):
  df['Src IP'] = df['Src IP'].replace(ips[i], int(netaddr.IPAddress(ips[i])))
print('loop over')

df['Flow Bytes/s'] = df['Flow Bytes/s'].astype('float')

print("---- HANDLING TIMESTAMPS -----")
print("len timestamps: " + str(len(df['Timestamp'])))
print(df.head())

df['Timestamp'] = df['Timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %I:%M:%S %p").timestamp())
# 29/01/2025 10:06:11 AM
df.to_csv('./out_data/own_UDP_clean.csv')
