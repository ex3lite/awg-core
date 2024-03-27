from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")

# Захватываем и анализируем пакеты
sniff(iface='wg0', filter='not port 22', prn=packet_callback, store=0)
