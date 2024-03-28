import psutil
import time


print(psutil.net_connections())
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
