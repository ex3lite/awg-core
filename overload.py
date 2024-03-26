import psutil

cpu_usage = psutil.cpu_percent(interval=1)  # За последнюю секунду


# Получаем информацию об использовании оперативной памяти
memory_info = psutil.virtual_memory()
total_memory = memory_info.total  # Всего оперативной памяти
used_memory = memory_info.used    # Используется оперативной памяти

memory_usage = (used_memory / total_memory) * 100
print(f"Нагрузка на процессор: {cpu_usage}")
print(f"Общий объем оперативной памяти: {total_memory} из них использовано {used_memory} это {int(memory_usage)}%")
print(f"Сервер был включен в: {psutil.boot_time()}")
print("Это уже обнова из гитхаба №4")
#print(f"")