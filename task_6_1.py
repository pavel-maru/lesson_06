
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# Задание 2_2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

from sys import getsizeof

# OS Windows 64-разрядная.
# Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
# Во всех трёх вариантах задачи вводится число 1234567890

# var.1
BASE = 10
DUO = 2
num = input('Введите натуральное число: ')
LENGTH = len(num)
num = int(num)
even, not_even = 0, 0

for i in range(LENGTH):
    digit = num % BASE ** (i + 1) // BASE ** (i)
    if digit % DUO == 0:
        even += 1
    else:
        not_even += 1

print(f'чётных цифр: {even}, нечётных цифр: {not_even}')
print(getsizeof(BASE), getsizeof(DUO), getsizeof(num), getsizeof(LENGTH),
      getsizeof(even), getsizeof(not_even), getsizeof(i), getsizeof(digit))

# Результат работы getsizeof: 14 14 18 14 14 14 14 14
# Общая сумма использованной памяти: 114 байт.

# var.2
DUO = 2
num = int(input('Введите натуральное число: '))
even, not_even = 0, 0

while num > 0:
    if num % DUO == 0:
        even += 1
    else:
        not_even += 1
    num = num // BASE

print(f'чётных цифр: {even}, нечётных цифр: {not_even}')
print(getsizeof(DUO), getsizeof(num), getsizeof(even), getsizeof(not_even))
# Результат работы getsizeof: 14 12 14 14
# num был преобразован из строкового типа в целочисленный, поэтому занял 12 байт вместо 18 (в предыдущем варианте)
#  Общая сумма использованной памяти: 54 байта.

# var.3
DUO = 2
digits = list(input('Введите натуральное число: '))
# print(type(digits))
even = []
not_even = []

for digit in digits:
    if int(digit) % DUO == 0:
        even.append(digit)
    else:
        not_even.append((digit))
# print(even, not_even)
print(f'чётных цифр: {len(even)}, нечётных цифр: {len(not_even)}')
print(getsizeof(DUO), getsizeof(digits), getsizeof(even), getsizeof(not_even), getsizeof(digit))
# Результат работы getsizeof: 14 68 60 60 26
# Три массива потребляют больше всего памяти.
# Общая сумма использованной памяти: 228 байт.

# Общий вывод: самая экономичная версия -  №2, с минимальным количеством переменных.
# Числовые переменные занимают меньше места, чем символьные аналогичной длины.
# Массивы (даже сформированные из тех же символов, что и строки) потребляют много памяти.

# # var.4
# DUO = 2
# num = input('Введите натуральное число: ')
# even, not_even = 0, 0
#
# for sym in num:
#     # print(sym, end=' ')
#     if int(sym) % DUO == 0:
#         even += 1
#     else:
#         not_even += 1
#
# print(f'чётных цифр: {even}, нечётных цифр: {not_even}')