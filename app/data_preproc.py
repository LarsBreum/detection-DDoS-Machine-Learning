import pandas as pd


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
print("min =", min(udpLag.shape,udp.shape,syn.shape,bios.shape,mssql.shape,ldap.shape))

ld = ldap.iloc[:191694,]
ld.to_csv('./7_classes/ldap7.csv')
f = portmap.iloc[:191694,]
f.to_csv('./7_classes/portmap7.csv')
a = mssql.iloc[:191694,]
a.to_csv('./7_classes/mssql7.csv')
b = bios.iloc[:191694,]
b.to_csv('./7_classes/bios7.csv')
c = syn.iloc[:191694,]
c.to_csv('./7_classes/syn7.csv')
d = udp.iloc[:191694,]
d.to_csv('./7_classes/udp7.csv')
e = udpLag.iloc[:191694,]
e.to_csv('./7_classes/udpLag7.csv')

# Working with 7 classes
ldap = pd.read_csv("./7_classes/ldap7.csv")
mssql = pd.read_csv("./7_classes/mssql7.csv")
bios = pd.read_csv("./7_classes/bios7.csv")
portmap = pd.read_csv("./7_classes/portmap7.csv")
syn = pd.read_csv("./7_classes/syn7.csv")
udp = pd.read_csv("./7_classes/udp7.csv")
udplag = pd.read_csv("./7_classes/udpLag7.csv")