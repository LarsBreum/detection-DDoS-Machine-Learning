import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

udp = pd.read_csv('./data/attack.csv')
udp_cols = list(udp.columns.values)

benign = pd.read_csv('./data/benign.csv')
benign_cols = list(benign.columns.values)



print("---- SHAPES ----")

min = min(udp.shape, benign.shape)
print("min =", min)


print("----- 7 CLASSES -----")

a = udp.iloc[:min[0],]
a.to_csv('./7_classes/attack.csv')
b = benign.iloc[:min[0],]
b.to_csv('./7_classes/benign.csv')


# Working with 7 classes
print("----- Reading 7_classes -----")
udp = pd.read_csv("./7_classes/attack.csv")
benign = pd.read_csv("./7_classes/benign.csv")


#checking for missing values
udp.isnull().sum()
benign.isnull().sum()


print(udp.describe())

ds = pd.concat([udp, benign])

ds.to_csv('./out_data/complete_dataset.csv')

print(ds.info())

print("---- WORKING WITH ENTIRE DATASET -----")
df = pd.read_csv('./out_data/complete_dataset.csv')

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
df=df.drop('Unnamed: 0',axis=1)
df=df.drop('Unnamed: 0.1',axis=1)
#df=df.drop('SimillarHTTP', axis=1)
df=df.drop('Flow ID', axis=1)
#df=df.drop('Timestamp', axis=1)


df['Label'] = df['Label'].replace('benign', '0')
df['Label'] = df['Label'].replace('UDP', '1')


#df['Label'] = df[' Label'].astype('int')
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
  converted.append(int(netaddr.IPAddress(ips[i])))
print("done")

#replacing ip in df with its decimal form
ips = df['Src IP'].unique()
l = len(ips)
print('starting loop, length is',l)

for i in range(l):
  df['Src IP'] = df['Src IP'].replace(ips[i], int(netaddr.IPAddress(ips[i])))
print('loop over')

df['Flow Bytes/s'] = df['Flow Bytes/s'].astype('float')



print("---- HANDLING Timestamps -----")
print("len Timestamps:" + str(len(df['Timestamp'])))

y=[]
m=[]
d=[]
h=[]
mi=[]
for i in range(len(df['Timestamp'])):
  a=int(df['Timestamp'][0][6:10])
  y.append(a)

  b= int(df['Timestamp'][0][3:5])
  m.append(b)

  c = int(df['Timestamp'][0][0:2])
  d.append(c)

  e= int(df['Timestamp'][0][11:13])
  h.append(e)

  f= int(df['Timestamp'][0][14:16])
  mi.append(f)

  if(i%1000==0):
    print('completed ',i)


df['year'] = y
df['month'] = m
df['day'] = d
df['hour'] = h
df['minute'] = mi

df.drop(columns = ['Timestamp'])

df.to_csv('./out_data/complete_dataset.csv')
