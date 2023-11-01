#For Linux
import os, socket

def get_domain_name(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"

f = open('list.txt', 'w')

IP = input("[+] Enter the host IP address:\t")
print("[+] Starting Ping Sweeper " + IP)
dot = IP.rfind(".")
IP = IP[0:dot + 1]
f = open(IP + '0' + '.txt', 'w')

for i in range(1, 255):
    host = IP + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
    domain_name = get_domain_name(host)
    if response == 0:
        print(host + " is up  "  + domain_name)
        f.write(host + " is up " + domain_name + "\n")
    else:
        print(host + " is down " + domain_name)
        f.write(host + " is down " + domain_name + "\n")
f.close()


