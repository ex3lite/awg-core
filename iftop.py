import pyshark

def packet_callback(pkt):
    try:
        print(pkt.ip.src, "->", pkt.ip.dst, ":", pkt.length)
    except AttributeError:
        pass  # Пропускаем пакеты без IP

capture = pyshark.LiveCapture(interface='wg0')
capture.apply_on_packets(packet_callback)