from wireguard_tools import WireguardKey
import ipaddress
import re
import subprocess
import json
import base64
import zlib
from datetime import timedelta

# WG_CONF_PATH = "/opt/amnezia/awg/wg0.conf"
# WG_PRIVATE_KEY_PATH = "/opt/amnezia/awg/wireguard_server_private_key.key"
# WG_PUBLIC_KEY_PATH = "/opt/amnezia/awg/wireguard_server_public_key.key"
# WG_PRESHARED_KEY_PATH = "/opt/amnezia/awg/wireguard_psk.key"

WG_CONF_PATH = "wg0.conf"
WG_PRIVATE_KEY_PATH = "wireguard_server_private_key.key"
WG_PUBLIC_KEY_PATH = "wireguard_server_public_key.key"
WG_PRESHARED_KEY_PATH = "wireguard_server_public_key.key"


def read_used_ip_addresses():
    # Функция для чтения файлов и извлечения IP-адресов
    ip_addresses = []
    with open(WG_CONF_PATH, 'r') as file:
        for line in file:
            if 'AllowedIPs' in line:
                ip_address = line.split('=')[1].strip()
                ip_addresses.append(ip_address)
    return ip_addresses


print(type(read_used_ip_addresses()))