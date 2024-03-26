import subprocess

# Отправляем запрос в консоль
command = "wg show"  # Пример команды, замените её на нужную вам
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

# Получаем ответ
output, error = process.communicate()

# Печатаем ответ
if output:
    print("Результат выполнения команды:")
    print(output.decode('utf-8'))
else:
    print("Произошла ошибка:")
    print(error.decode('utf-8'))
