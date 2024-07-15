from operator import xor
from time import sleep

from scapy.all import fragment
from scapy.all import *


MAX_MSG_SIZE=62

msg="MESSAGE"

pkt=IP(dst="SERVER_IP")/UDP(dport=SERVER_PORT)/msg
print(len(pkt))
xor = 0
i=0
list_xor=[]
frags=fragment(pkt,fragsize=30)
for f in frags:
    while i < len(f[Raw].load):
        xor=xor ^ ((f[Raw].load)[i])
        i+=1
    list_xor.append(xor)
    print(len(f))
    print(f)
    send(f)
    i=0
    xor=0
    sleep(3)

xor_sum=list_xor[0]

print(list_xor)

for x in list_xor:
    xor_sum=xor_sum ^ x

print(xor_sum)

msg="xor is :%d"%(xor_sum) 

pkt=IP(dst="SERVER_IP")/UDP(dport=SERVER_PORT)/msg

send(pkt)