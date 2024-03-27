import pyshark

# Открыть файл pcap
cap = pyshark.FileCapture('example.pcap')

# Выбрать все пакеты HTTP
http_packets = cap.filter('http')

# Печать информации о каждом пакете HTTP
for packet in http_packets:
    print('---')
    print('Источник:', packet.ip.src)
    print('Назначение:', packet.ip.dst)
    print('Метод HTTP:', packet.http.request_method)
    print('URI HTTP:', packet.http.request_uri)
    print('Код ответа HTTP:', packet.http.response_code)

# Закрыть файл pcap
cap.close()