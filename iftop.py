import time
import psutil
import sqlite3
import datetime
import subprocess
import ipaddress
import scapy.all as scapy

SQLBase = "database.db"

def give_endpoint(local_ip:str)->str:
    output = subprocess.check_output(f"wg show wg0 dump | grep '{local_ip}' | awk '{{print $3}}'", shell=True, universal_newlines=True)
    if output != "(none)" or output != "":
        return output
    else:
        return "none"
def is_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False
    
def iftop():
  # Считывание 10 пакетов с интерфейса wg0  
    for packet in scapy.sniff(iface="wg0", count=10):
        # Печать информации о IP-адресах
        
        Sender          = give_endpoint(packet[scapy.IP].src) if is_private_ip(packet[scapy.IP].src) else packet[scapy.IP].src
        Recipient       = give_endpoint(packet[scapy.IP].dst) if is_private_ip(packet[scapy.IP].dst) else packet[scapy.IP].dst

        PacketSize      = len(packet)
        DateTime        = int(packet.time)
        Protocol        = 'TCP' if scapy.TCP in packet else 'UDP' if scapy.UDP in packet else 'OTHER'
        UUID            = "none"

        print(f"\n{return_time_now()}| Вывод информации о пакете:")
        print(f"{Sender}    ->{Recipient}")
        print(f"Protocol    : {Protocol}")

    
        if scapy.TCP in packet:
            # Печать информации о портах
            print(f"{packet[scapy.TCP].sport} -> {packet[scapy.TCP].dport}")
            # Печать информации о размере пакета\
            print(f"Packet size : {len(packet)} bytes")
            # Печать информации о времени
            print(f"Time        : {packet.time}")

        # Запись информации о пакете в базу данных
        SQL = SQLiteOperation(SQLBase)
        SQL.write_packet_information(UUID, Sender, Recipient, Protocol, PacketSize, DateTime)

def return_time_now()->str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class SQLiteOperation:
    def __init__(self, database:str):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        print(f"{return_time_now()}| База данных подключена")

    def write_packet_information(self, UUID:str, Sender:str, Recipient:str, Protocol:str, SizePacket:int, DateTime:int)->bool:
        with self.connection:
            self.cursor.execute("INSERT INTO traffic (UUID, Sender, Recipient, Protocol, SizePacket, DateTime) VALUES (?, ?, ?, ?, ?, ?)", (UUID, Sender, Recipient, Protocol, SizePacket, DateTime))

        print(f"{return_time_now()}| Информация о пакете записана в базу данных")
        return True


    def __del__(self):
        self.connection.close()
        print(f"{return_time_now()}| База данных отключена")

# Бесконечный цикл
while True:
    iftop()
    time.sleep(1)


