import psutil
import time

def track_traffic(interface):
    while True:
        # Получаем список активных сетевых соединений
        connections = psutil.net_connections(kind='inet')

        # Создаем множество для хранения уникальных IP-адресов отправителей и получателей
        src_ips = set()
        dst_ips = set()

        # Анализируем сетевые соединения и добавляем IP-адреса в соответствующие множества
        for conn in connections:
            if conn.fd == -1 or conn.type != psutil.SOCK_STREAM:
                continue
            if conn.laddr and conn.laddr.ip == interface:
                src_ips.add(conn.raddr.ip)
            if conn.raddr and conn.raddr.ip == interface:
                dst_ips.add(conn.laddr.ip)

        # Выводим список уникальных IP-адресов отправителей и получателей
        print("Incoming traffic from:")
        for ip in src_ips:
            print(f"  {ip}")
        print("Outgoing traffic to:")
        for ip in dst_ips:
            print(f"  {ip}")

        # Ждем некоторое время перед обновлением информации
        time.sleep(1)

# Укажите интерфейс, который вы хотите отслеживать
selected_interface = 'wg0'

# Вызываем функцию для отслеживания трафика на выбранном интерфейсе
track_traffic(selected_interface)
