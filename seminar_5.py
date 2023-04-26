# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
#def fibo1(number):
#     list = []
#     list.append(1)
#     list.append(1)
#     for i in range(2, number + 1):
#         list.append(list[i - 1] + list[i - 2])
#     return list[number]

# number = int(input('Enter a number: '))
# print(fibo1(7))

# def fibo2(number):
#     count = 2
#     a, b = 1, 1
#     while count <= number:
#         result = a + b
#         b = a
#         a = result
#         count += 1
#     return result

# number = int(input('Enter a number: '))
# print(fibo2r(7))

# def fibo_recur(number):
#     while number >= 2:
#         return fibo_recur(number - 1) + fibo_recur(number - 2)
#     else:
#         return 1

# number = int(input('Enter a number: '))
# print(fibo_recur(number))


# 


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Reshenye 1
# my_list = [1, 3, 4, 3, 4, 4, 4]
# def swap (list):
#     for i in range(list.count(max(list))):
#         list[list.index(max(list))] = min(list)
#     return list
# print(swap(my_list))




# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: ye

# number = int(input('Enter a number: '))

# def find_simple(number):
#     count = 0
#     for i in range(1, number + 1):
#         if count > 2:
#             break
#         elif number % i == 0:
#             count += 1
#     return True if count <= 2 or number == 1 else False
# print(find_simple(number))

# def is_simple(number):
#     for i in range(2, number//2 + 1):
#         if number % i == 0:
#             return False
#     return True
# print(is_simple(number))



# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# number = int(input('Enter a number: '))
def rev_inp(input_number):
    if input_number == 1:
        value = input()
        return value
    value = input()
    return rev_inp(input_number - 1) + ' ' + value
number = int(input('Enter a number: '))
print(f'Enter {number} value(s)')
print(rev_inp(number))