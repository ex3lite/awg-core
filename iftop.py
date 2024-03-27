import psutil
import time

def iftop():
    while True:
        # Получаем информацию о сетевом трафике
        net_io = psutil.net_io_counters(pernic=True)

        print("Network Traffic:")
        for interface, io in net_io.items():
            print(f"Interface: {interface}")
            print(f"  Sent: {io.bytes_sent} bytes")
            print(f"  Received: {io.bytes_recv} bytes")

        # Ждем некоторое время перед обновлением информации
        time.sleep(1)

# Вызываем функцию iftop для отслеживания трафика
iftop()
