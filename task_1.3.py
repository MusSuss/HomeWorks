# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

# Решение:

def get_days_in_month(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return None

month_number = int(input("Введите номер месяца: "))
month_name = ""
days_in_month = get_days_in_month(month_number)

if month_number == 1:
    month_name = "январь"
elif month_number == 2:
    month_name = "февраль"
elif month_number == 3:
    month_name = "март"
elif month_number == 4:
    month_name = "апрель"
elif month_number == 5:
    month_name = "май"
elif month_number == 6:
    month_name = "июнь"
elif month_number == 7:
    month_name = "июль"
elif month_number == 8:
    month_name = "август"
elif month_number == 9:
    month_name = "сентябрь"
elif month_number == 10:
    month_name = "октябрь"
elif month_number == 11:
    month_name = "ноябрь"
elif month_number == 12:
    month_name = "декабрь"

if days_in_month is not None:
    print("Вы ввели", month_name + ".")
    print("В этом месяце", days_in_month, "дней.")
else:
    print("Такого месяца нет!")