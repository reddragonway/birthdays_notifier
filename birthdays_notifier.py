# импорт модуля
import datetime
# выводим заголовок
print("=== Дни Рождения ===")
# определяем сегодняшнюю дату в формате ДД-ММ
today = datetime.date.today()
today = str(today)
today = '.'.join(list(reversed(today.split('-')))[:-1])
# вспомогательный счетчик
i = 0
# открываем файл birthdays.txt и считываем его построчно
b_file = open("C:\Birthdays_notifier\source_birthdays.txt", encoding="UTF-8")
b_data = b_file.read().splitlines()
# каждую строчку переводим в формат ДД-ММ
for line in b_data:
    birthday = str(line).split(":")
    b_name = birthday[0]
    b_date = birthday[1]
    if b_date == today:  # если сегодняшняя дата совпадает с датой b_date, выводим сообщение
        print(f"Сегодня день рождения у {b_name}")
        i = i + 1  # увеличиваем счетчик каждый раз когда выводим сообщение
# если счетчик равен 0, значит ДР сегодня нет
if i == 0:
    print("Сегодня именинников нет...")
# закрываем файл
b_file.close()
# выводим приглашение выйти и программы
print("")
input("Для выхода из программы нажмите ENTER...")
