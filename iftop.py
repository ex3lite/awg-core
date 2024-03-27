import psutil
import time

def iftop():
    while True:
        # Получаем информацию о сетевом трафике для указанного интерфейса
        io = psutil.net_io_counters()["wg0"]
        print(f"  Sent: {io.packets_sent}")
        print(f"  Received: {io.packets_recv}")

        # Ждем некоторое время перед обновлением информации
        time.sleep(1)

# Вызываем функцию iftop с указанным интерфейсом для отслеживания трафика
iftop()
