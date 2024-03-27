import psutil
import time

def track_traffic(interface):
    while True:
        # Получаем информацию о сетевом трафике для указанного интерфейса
        io = psutil.net_io_counters(pernic=True)[interface]

        print("Traffic on interface", interface)
        print(f"  Sent from: {io.bytes_sent} bytes")
        print(f"  Received by: {io.bytes_recv} bytes")

        # Получаем список активных сетевых соединений
        connections = psutil.net_connections(kind='inet')

        # Создаем множество для хранения уникальных IP-адресов отправителей и получателей
        src_ips = set()
        dst_ips = set()

        # Анализируем сетевые соединения и добавляем IP-адреса в соответствующие множества
        for conn in connections:
            if conn.family == psutil.AF_INET and conn.laddr and conn.laddr[0] == interface:
                src_ips.add(conn.laddr[0])
            if conn.family == psutil.AF_INET and conn.raddr and conn.raddr[0] == interface:
                dst_ips.add(conn.raddr[0])

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
