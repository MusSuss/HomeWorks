# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Решение:
print("Пункт A")

import random
random_songs = random.sample(my_favorite_songs, 3)
print(f"Случайные песни: {random_songs}")

total = 0
for time in random_songs:
    total += time[1]
total = round(total, 2)
print(f"Три песни звучат {total} минут")

import datetime
total_time = datetime.timedelta()
for song in random_songs:
 minutes = int(song[1])
 seconds = round((song[1] - minutes) * 100)
 song_time = datetime.timedelta(minutes=minutes, seconds=seconds)
 total_time += song_time
print(f"В формате времени: {total_time}")


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение:
print("Пункт B")

random_songs_dict = random.sample(list(my_favorite_songs_dict.items()), k=3)
print(f"Случайные песни: {random_songs_dict}")

total_dict = 0
for time in random_songs_dict:
    total_dict += time[1]
total_dict = round(total_dict, 2)
print(f"Три песни звучат {total_dict} минут")

total_time_dict = datetime.timedelta()
for song in random_songs_dict:
 minutes = int(song[1])
 seconds = round((song[1] - minutes) * 100)
 song_time_dict = datetime.timedelta(minutes=minutes, seconds=seconds)
 total_time_dict += song_time_dict
print(f"В формате времени: {total_time_dict}")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Решение:
# для пункта A - строки 24-26
# для пункта B - строки 64-65

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Решение:
# для пункта A - строки 34-41
# для пункта B - строки 73-79
