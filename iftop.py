import subprocess

# Запуск iftop в subprocess
process = subprocess.Popen(["iftop", "-i", "wg0"], stdout=subprocess.PIPE)

# Чтение вывода iftop построчно
for line in process.stdout:
    print(line.decode("utf-8").strip())

# Закрытие subprocess
process.terminate()
