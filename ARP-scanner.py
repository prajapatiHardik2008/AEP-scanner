from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
import sys
def scan(ip_range):
    print(f"[*] {ip_range} Scanning ..... ")
    ARP_requ =  ARP(pdst=ip_range)
    brodcast = Ether(dst="ff.ff.ff.ff.ff.ff")
    packet = brodcast / ARP_requ
    result = srp(packet,timeout= 2,verbose=False)[0]

    clients = []
    for send , recev in result:
        clients.append({"ip":recev.psrc,"mac":recev.hwsrc})
    
    return clients
def display(result):
    print("\nIP Address\t\tMAC Address")
    print("-" * 40)
    for client in result:
        print(f"{client['ip']}\t\t{client['mac']}")


if __name__ == "__main__":
    if len(sys.argv )!= 2:
        print("Usage :- $ python ARP-scanner.py <IP_range>")
        print("Example :- & python ARP-scanner.py 192.168.1.1/24")
    else:
        ip_range = sys.argv[1]
        result = scan(ip_range)
        result
        display(result)
        