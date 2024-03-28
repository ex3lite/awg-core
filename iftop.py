import time

import scapy.all as scapy

def iftop():
  # Считывание 10 пакетов с интерфейса wg0  
    for packet in scapy.sniff(iface="wg0", count=10):
        # Печать информации о IP-адресах
        print(packet[scapy.IP].src, packet[scapy.IP].dst)
        # Печать информации о портах
        print(packet[scapy.TCP].sport, packet[scapy.TCP].dport)
        # Печать информации о размере пакета
        print(len(packet))
        # Печать информации о времени
        print(packet.time)

# Бесконечный цикл
while True:
    iftop()
    time.sleep(1)


