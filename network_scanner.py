import scapy.all as scapy
import argparse
from prettytable import PrettyTable


def find_ip(target):
    arp_request = scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_braodcast = broadcast / arp_request
    list = scapy.srp(arp_braodcast, timeout=1, verbose=False)[0]

    devices = []
    for element in list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices.append(device_info)

    table = PrettyTable(["IP Address", "MAC Adress"])
    
    for device in devices:
        table.add_row([device["ip"], device["mac"]])

    print(table)

def main():
    parset = argparse.ArgumentParser(description="IM TRYING TO DO NETWORK SCANNER")
    parset.add_argument("target", help="Target IP range (moje bi 192.168.1.1/24)")
    arg = parset.parse_args()

    print("\nScanning network...\n")
    find_ip(arg.target)

if __name__ == "__main__":
    main()