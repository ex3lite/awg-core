import pyshark

# Словарь для отслеживания потребления трафика по IP-адресам
traffic_usage = {}

def packet_callback(pkt):
    try:
        src_ip = pkt.ip.src
        dst_ip = pkt.ip.dst
        length = int(pkt.length)

        # Обновляем потребление трафика для отправителя и получателя
        traffic_usage[src_ip] = traffic_usage.get(src_ip, 0) + length
        traffic_usage[dst_ip] = traffic_usage.get(dst_ip, 0) + length
    except AttributeError:
        pass  # Пропускаем пакеты без IP

def print_traffic_report():
    print("Traffic Report:")
    for ip, usage in traffic_usage.items():
        print(f"{ip}: {usage} bytes")

# Открываем сетевой интерфейс для захвата пакетов
capture = pyshark.LiveCapture(interface='wg0', bpf_filter='not port 22', tshark_path='/usr/bin/tshark')

# Захватываем и обрабатываем пакеты
capture.apply_on_packets(packet_callback)

# Печатаем краткий отчет о потреблении трафика
print_traffic_report()
