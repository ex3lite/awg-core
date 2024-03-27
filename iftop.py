import psutil
import time

def print_network_traffic():
    # Получить список всех активных соединений
    connections = psutil.net_connections()

    for connection in connections:
        local_address = connection.laddr
        remote_address = connection.raddr
        if remote_address:
            print(f"Локальный адрес: {local_address.ip}:{local_address.port}")
            print(f"Удаленный адрес: {remote_address.ip}:{remote_address.port}")
            print("-----")

print_network_traffic()