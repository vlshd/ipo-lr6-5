import random

list = [random.randint(-50, 50) for _ in range(25)] # cоздание списка случайных целых чисел
plus = len([num for num in list if num > 0]) # подсчет количества положительных
minus = len([num for num in list if num < 0]) # подсчет количества отрицательных
zero = len([num for num in list if num == 0]) # подсчет количества нулевых

total_count = len(list) # возвращает количество элементов в списке
plus_percent = (plus / total_count) * 100 # процент положительных
minus_percent = (minus / total_count) * 100 # процент отрицательных
zero_percent = (zero / total_count) * 100 # процент нулевых

max = max(list) # самое большое значение
min = min(list) # самое маленькое значение

print("Список случайных чисел:", list) # вывод
print(f"Положительных чисел: {plus} ({plus_percent:.2f}%)") # вывод
print(f"Отрицательных чисел: {minus} ({minus_percent:.2f}%)") # вывод
print(f"Нулевых элементов: {zero} ({zero_percent:.2f}%)") # вывод
print(f"Самое большое значение: {max}") # вывод
print(f"Самое маленькое значение: {min}") # вывод
