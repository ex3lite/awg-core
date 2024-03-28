import time
import psutil
import sqlite3
import datetime
import subprocess
import scapy.all as scapy

SQLBase = "database.db"

def give_endpoint(local_ip:str)->str:
    output = subprocess.check_output(f"wg show wg0 dump | grep '{local_ip}' | awk '{{print $3}}'", shell=True, universal_newlines=True)
    if output != "(none)" or output != "":
        return output
    else:
        return "none"

def iftop():
  # Считывание 10 пакетов с интерфейса wg0  
    for packet in scapy.sniff(iface="wg0", count=10):
        # Печать информации о IP-адресах
        
        Sender          = packet[scapy.IP].src
        Sender_Port     = 0

        EndPoint        = give_endpoint(Sender)

        print(f"EndPoint: {EndPoint}")
        Recipient       = packet[scapy.IP].dst
        Recipient_Port  = 0

        PacketSize      = len(packet)
        DateTime        = packet.time
        Protocol        = 'TCP' if scapy.TCP in packet else 'UDP' if scapy.UDP in packet else 'OTHER'

        print(f"\n{return_time_now()}| Вывод информации о пакете:")
        print(f"{packet[scapy.IP].src} -> {packet[scapy.IP].dst}")
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
        #SQL.write_packet_information(Sender, Sender_Port, Recipient, Recipient_Port, PacketSize, DateTime, Protocol)

def return_time_now()->str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class SQLiteOperation:
    def __init__(self, database:str):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        print(f"{return_time_now()}| База данных подключена")

    def write_packet_information(self, Sender:str, Sender_Port:int, Recipient:str, Recipient_Port:int, Size:int, DateTime:int, Protocol:str)->bool:
        with self.connection:
            self.cursor.execute("INSERT INTO traffic (Sender, Sender_Port, Recipient, Recipient_Port, Size, DateTime, Protocol) VALUES (?, ?, ?, ?, ?, ?, ?)", (Sender, Sender_Port, Recipient, Recipient_Port, Size, DateTime, Protocol))

        print(f"{return_time_now()}| Информация о пакете записана в базу данных")
        return True

    def __del__(self):
        self.connection.close()
        print(f"{return_time_now()}| База данных отключена")

# Бесконечный цикл
while True:
    iftop()
    time.sleep(1)


