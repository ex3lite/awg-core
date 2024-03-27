import psutil
import time

def iftop(interface):
    while True:
        # Получаем информацию о сетевом трафике для указанного интерфейса
        io = psutil.net_io_counters(pernic=True)[interface]

        print("Network Traffic for", interface)
        print(f"  Sent: {io.bytes_sent} bytes")
        print(f"  Received: {io.bytes_recv} bytes")

        # Ждем некоторое время перед обновлением информации
        time.sleep(1)

# Укажите интерфейс, который вы хотите мониторить
selected_interface = 'wg0'

# Вызываем функцию iftop с указанным интерфейсом для отслеживания трафика
iftop(selected_interface)
