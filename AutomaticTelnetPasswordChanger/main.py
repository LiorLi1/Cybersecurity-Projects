import telnetlib
import netifaces
import nmap
import json
import string
import random
import ipaddress

nm=nmap.PortScanner()
net=netifaces.interfaces()
ips=[]
for interface in net:
    try:
        for x in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
            print(x)
            ips.append(x)
    except:
        continue

tempHosts=[]
hosts=[]
for i in ips:
    tempHosts.append(str(ipaddress.IPv4Network(i['addr']+'/'+i['netmask'],False)))

print(tempHosts)


for th in tempHosts:
    try:
     nm.scan(th,'23',timeout=300)
     for host in nm.all_hosts():
         if nm[host]['tcp'][23]['state'] == 'open' and nm[host]['tcp'][23]['name'] == 'telnet':
             hosts.append(host)
    except:
        continue



characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")
length=8


with open('defaults.json') as file:
    data=json.load(file)

for h in hosts:
    for p in data['users']:
        tn=telnetlib.Telnet(h)
        tn.open(h)
        print(tn.read_until(b"login: ").decode('ascii'))
        tn.write(p['user'].encode('ascii')+b"\n")
        print(tn.read_until(b"Password: ",timeout=10).decode('ascii'))
        tn.write(p['password'].encode('ascii')+b"\n")
        if b"Login incorrect" in tn.read_until(b"Login incorrect",timeout=10):
            print("Username and/or password are secure. Skipping...")
            tn.close()
            continue
        else:
            print(tn.read_until(b"$ ",timeout=10).decode('ascii'))
            ans=input("Username or password are unsecured. Do you want to change your password?(y/n): ")
            if ans=='n':
                print("Skipping...\n")
                tn.close()
                continue
            else:
                print("Generating new password...\n")
                random.shuffle(characters)
                password=[]
                for i in range(length):
                    password.append(random.choice(characters))
                random.shuffle(password)
                newPassword="".join(password)
                print("Generated password: "+newPassword)
                tn.write(b"passwd\n")
                print(tn.read_until(b": ").decode('ascii'))
                tn.write(p['password'].encode('ascii')+b"\n")
                print(tn.read_until(b": ").decode('ascii'))
                tn.write(newPassword.encode('ascii')+b"\n")
                print(tn.read_until(b": ").decode('ascii'))
                tn.write(newPassword.encode('ascii') + b"\n")
                print(tn.read_until(b"$ ").decode('ascii'))
                tn.close()
                continue
file.close()

































