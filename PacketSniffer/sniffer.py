from scapy.all import *


def packet_callback(packet):
    print(packet.show())

def main():
    sniff(prn=packet_callback,filter='udp and port CLIENT_PORT and host CLIENT_IP',count=100)
    
        

if __name__=='__main__':
    main()
