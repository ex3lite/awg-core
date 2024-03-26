import psutil
import sqlite3
import datetime

SQLBase = "database.db"

class SQLiteOperation:
    def __init__(self, database:str):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        print(f"{return_time_now()}| База данных подключена")


    def write_system_information(self, ram_used:int, ram_total:int, cpu_usage:int, network_load:int, datetime_operation:int, boot_uptime:int, size_db:int)->bool:
        with self.connection:
            self.cursor.execute("INSERT INTO overload (ram_used, ram_total, cpu_usage, network_load, datetime_operation, boot_uptime, size_db) VALUES (?, ?, ?, ?, ?, ?, ?)", (ram_used, ram_total, cpu_usage, network_load, datetime_operation, boot_uptime, size_db))

        print(f"{return_time_now()}| Информация о системе записана в базу данных")
        return True
    
    def write_log_event(self, event:str, status_code:int, data_time:int)->bool:
        with self.connection:
            self.cursor.execute("INSERT INTO logs (event, status_code, data_time) VALUES (?, ?, ?)", (event, status_code, data_time))
        print(f"{return_time_now()}| Событие записано в лог")
        return True

    def __del__(self):
        self.connection.close()
        print(f"{return_time_now()}| База данных отключена")


def return_time_now()->str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class system_information:
    def __init__(self) -> None:
        self.cpu_usage = psutil.cpu_percent(interval=1)
        self.memory_info = psutil.virtual_memory()
        self.total_memory = self.memory_info.total  
        self.used_memory = self.memory_info.used
        self.memory_usage = (self.used_memory / self.total_memory) * 100
        self.network_load = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        self.datetime_operation = datetime.datetime.now().timestamp()
        self.boot_uptime = psutil.boot_time()
        print(f"{return_time_now()}| Информация о системе получена")
        print(f"┌─────────────────────────────────────────┐")
        print(f"│► СВОДКА ПОЛУЧЕННОЙ ИНФОРМАЦИИ О СИСТЕМЕ │")
        print(f"├───────────────────┬─────────────────────┤")
        print(f"│ CPU Load          │ {int(self.cpu_usage)}%")
        print(f"├───────────────────┼─────────────────────┤")
        print(f"│ Total RAM memory  │ {self.total_memory}")
        print(f"│ Used RAM memory   │ {self.used_memory}")
        print(f"│ % Usage memory    │ {int(self.memory_usage)}%")
        print(f"├───────────────────┼─────────────────────┤")
        print(f"│ Network load      │ {self.network_load}")
        print(f"├───────────────────┼─────────────────────┤")
        print(f"│ Date time UNIX    │ {int(self.datetime_operation)}")
        print(f"│ Boot time UNIX    │ {int(self.boot_uptime)}")
        print(f"└───────────────────┴─────────────────────┘")
        #self.size_db = 

    def write_system_information(self):
        SQLWrite = SQLiteOperation(SQLBase)
        SQLWrite.write_system_information(self.used_memory, self.total_memory, self.cpu_usage, self.network_load, self.datetime_operation, self.boot_uptime, 0)
        print(f"{return_time_now()}| Отправлено на запись в базу данных")


if __name__ == "__main__":
    SystemInfo = system_information()
    SystemInfo.write_system_information()
    pass
