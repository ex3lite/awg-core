import psutil
import time


print(psutil.net_connections())
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())

# Get all network connections
connections = psutil.net_connections()

for connection in connections:
    # Filter out the connections that are not established
    if connection.status == psutil.CONN_ESTABLISHED:
        local_address = f"{connection.laddr.ip}:{connection.laddr.port}"
        remote_address = f"{connection.raddr.ip}:{connection.raddr.port}" if connection.raddr else 'N/A'
        print(f"Local address: {local_address} is sending packets to Remote address: {remote_address}")
        while True:
            connections = psutil.net_connections()
            for connection in connections:
                if connection.status == psutil.CONN_ESTABLISHED:
                    local_address = f"{connection.laddr.ip}:{connection.laddr.port}"
                    remote_address = f"{connection.raddr.ip}:{connection.raddr.port}" if connection.raddr else 'N/A'
                    print(f"Local address: {local_address} is sending packets to Remote address: {remote_address}")
            time.sleep(1)  # Pause for 1 second before repeating the loop