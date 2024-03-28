import time

import scapy.all as scapy

def iftop():
  # Считывание 10 пакетов с интерфейса wg0  
    for packet in scapy.sniff(iface="wg0", count=10):
        # Печать информации о IP-адресах
        print(f"\n Вывод информации о пакете:")
        print(f"{packet[scapy.IP].src} -> {packet[scapy.IP].dst}")
        if scapy.TCP in packet:
            # Печать информации о портах
            print(f"{packet[scapy.TCP].sport} -> {packet[scapy.TCP].dport}")
            # Печать информации о размере пакета\
            print(f"Packet size: {len(packet)} bytes")
            # Печать информации о времени
            print(f"Time: {packet.time}")

# Бесконечный цикл
while True:
    iftop()
    time.sleep(1)


