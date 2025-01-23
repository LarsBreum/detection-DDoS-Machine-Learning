import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#df=pd.read_csv('./clean.csv')

udp = pd.read_csv('./data/DrDoS_UDP.csv')
udp_cols = list(udp.columns.values)

ssdp = pd.read_csv('./data/DrDoS_SSDP.csv')
ssdp_cols = list(ssdp.columns.values)

snmp = pd.read_csv('./data/DrDoS_SNMP.csv')
snmp_cols = list(snmp.columns.values)

ntp = pd.read_csv('./data/DrDoS_NTP.csv')
ntp_cols = list(ntp.columns.values)

bios = pd.read_csv('./data/DrDoS_NetBIOS.csv')
bios_cols = list(bios.columns.values)

mssql=pd.read_csv('./data/DrDoS_MSSQL.csv')
mssql_cols = list(mssql.columns.values)

ldap=pd.read_csv('./data/DrDoS_LDAP.csv')
ldap_cols = list(ldap.columns.values)

dns=pd.read_csv('./data/DrDoS_DNS.csv')
dns_cols = list(dns.columns.values)

syn = pd.read_csv('./data/Syn.csv')
syn_cols = list(syn.columns.values)

portmap = pd.read_csv('./data/Portmap.csv')
portmap_cols = list(portmap.columns.values)

udpLag = pd.read_csv('./data/UDPLag.csv')
udpLag_cols = list(udpLag.columns.values)

udp = pd.read_csv('./data/UDP.csv')
udp_cols = list(udp.columns.values)

print("---- SHAPES ----")
print("LDAP= ",ldap.shape)
print("MSSQL= ",mssql.shape)
print("BIOS= ",bios.shape)
print("Portmap= ",portmap.shape)
print("SYN= ",syn.shape)
print("UDP= ",udp.shape)
print("UDPLag= ",udpLag.shape)
min = min(udpLag.shape,udp.shape,syn.shape,bios.shape,mssql.shape,ldap.shape)
print("min =", min)


print("----- 7 CLASSES -----")
ld = ldap.iloc[:min[0],]
ld.to_csv('./7_classes/ldap7.csv')
f = portmap.iloc[:min[0],]
f.to_csv('./7_classes/portmap7.csv')
a = mssql.iloc[:min[0],]
a.to_csv('./7_classes/mssql7.csv')
b = bios.iloc[:min[0],]
b.to_csv('./7_classes/bios7.csv')
c = syn.iloc[:min[0],]
c.to_csv('./7_classes/syn7.csv')
d = udp.iloc[:min[0],]
d.to_csv('./7_classes/udp7.csv')
e = udpLag.iloc[:min[0],]
e.to_csv('./7_classes/udpLag7.csv')

# Working with 7 classes
print("----- Reading 7_classes -----")
ldap = pd.read_csv("./7_classes/ldap7.csv")
mssql = pd.read_csv("./7_classes/mssql7.csv")
bios = pd.read_csv("./7_classes/bios7.csv")
portmap = pd.read_csv("./7_classes/portmap7.csv")
syn = pd.read_csv("./7_classes/syn7.csv")
udp = pd.read_csv("./7_classes/udp7.csv")
udplag = pd.read_csv("./7_classes/udpLag7.csv")

#checking for missing values
ldap.isnull().sum()
mssql.isnull().sum()
bios.isnull().sum()
portmap.isnull().sum()
syn.isnull().sum()
udp.isnull().sum()
udplag.isnull().sum()

print(ldap.describe())

ds = pd.concat([ldap, mssql, bios, portmap, syn, udp, udplag])

ds.to_csv('./out_data/complete_dataset.csv')

print(ds.info())

print("---- WORKING WITH ENTIRE DATASET -----")
df = pd.read_csv('./out_data/complete_dataset.csv')

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
df=df.drop('Unnamed: 0.1',axis=1)
df=df.drop('SimillarHTTP', axis=1)
df=df.drop('Flow ID', axis=1)
#df=df.drop(' Timestamp', axis=1)


# df['Label'] = df[' Label'].replace('BENIGN', '0')
# df['Label'] = df[' Label'].replace('NetBIOS', '1')
# df['Label'] = df[' Label'].replace('LDAP', '2')
# df['Label'] = df[' Label'].replace('MSSQL', '3')
# df['Label'] = df[' Label'].replace('Portmap', '4')
# df['Label'] = df[' Label'].replace('Syn', '5')
# df['Label'] = df[' Label'].replace('UDP', '6')
# df['Label'] = df[' Label'].replace('UDPLag', '7')

df['Label'] = df[' Label'].replace('BENIGN', '0')
df['Label'] = df[' Label'].replace('DrDos_NetBIOS', '1')
df['Label'] = df[' Label'].replace('DrDoS_LDAP ', '2')
df['Label'] = df[' Label'].replace('DrDos_MSSQL', '3')
df['Label'] = df[' Label'].replace('Portmap', '4')
df['Label'] = df[' Label'].replace('Syn', '5')
df['Label'] = df[' Label'].replace('UDP', '6')
df['Label'] = df[' Label'].replace('UDPLag', '7')

#df['Label'] = df[' Label'].astype('int')
print(df.Label.unique())

print("Print label value counts:")
print(df.Label.value_counts())

df.to_csv('./out_data/complete_dataset.csv')

print('num = ',len(df[' Source IP'].unique()))
df[' Source IP'].unique()
le = LabelEncoder()
a = df



import netaddr
print(int(netaddr.IPAddress('192.168.4.54')))
ips = df[' Destination IP']
converted=[]
for i in range(len(ips)):
  converted.append(int(netaddr.IPAddress(ips[i])))
print("done")

#replacing ip in df with its decimal form
ips = df[' Source IP'].unique()
l = len(ips)
print('starting loop, length is',l)

for i in range(l):
  df[' Source IP'] = df[' Source IP'].replace(ips[i], int(netaddr.IPAddress(ips[i])))
print('loop over')

df['Flow Bytes/s'] = df['Flow Bytes/s'].astype('float')

print("---- HANDLING TIMESTAMPS -----")
print("len timestamps:" + str(len(df[' Timestamp'])))

y=[]
m=[]
d=[]
h=[]
mi=[]
for i in range(len(df[' Timestamp'])):
  a=int(df[' Timestamp'][0][0:4])
  y.append(a)

  b= int(df[' Timestamp'][0][5:7])
  m.append(b)

  c = int(df[' Timestamp'][0][8:10])
  d.append(c)

  e= int(df[' Timestamp'][0][11:13])
  h.append(e)

  f= int(df[' Timestamp'][0][14:16])
  mi.append(f)

  if(i%1000==0):
    print('completed ',i)

mi = pd.DataFrame(mi)
print(mi.describe())

