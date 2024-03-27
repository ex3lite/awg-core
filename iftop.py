import pcapy
from struct import unpack
from socket import inet_ntoa

def handle_packet(header, data):
    # Извлекаем IP-заголовок
    ip_header = data[14:34]  # Предполагаем, что это Ethernet-фрейм
    iph = unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    src_ip = inet_ntoa(iph[8])
    dst_ip = inet_ntoa(iph[9])

    print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")

# Открываем сетевой интерфейс для захвата пакетов
cap = pcapy.open_live('wg0', 65536, True, 100)

# Настраиваем фильтр для исключения порта 22 (SSH)
cap.setfilter('not port 22', 0, 0)

# Захватываем и обрабатываем пакеты
while True:
    header, packet = cap.next()
    handle_packet(header, packet)
