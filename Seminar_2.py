# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input:       5

# Output:    120

# Решение 1

# n = int (input("Введите число : "))
# factorial = 1
# while n>1: 
#      factorial = factorial*n # factorial*= n
#      n= n - 1     # n-=1
# print(f"Полученный факториал: {factorial}")

# Решение 2

# a=int(input("Введите число: "))
# count = 1
# while a>1:    
#     count = count*a  # factorial*=a
#     a-=1
# print(count)
# print("цикл окончен")

# Решение 3

# print("Введите N:")
# n = int(input())
# mult = 1
# while n > 0:
#     mult = mult * n
#     n = n - 1
#     # print(f"n = {n}, mult = {mult}")
# print(mult if (n == 0) else "Ведите положительное число")

# Задание 
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input:     5

# Output:  6

# Решение 1
# print("Введите число A:")
# numb = int(input())
# fib1 = fib2 = 1
# fib_sum = 2
# fib_idx = 2

# while fib2 < numb:
#     # fib1, fib2 = fib2, fib2 + fib1
#     fib_sum = fib2 + fib1
#     fib1 = fib2
#     fib2 = fib_sum
#     fib_idx += 1
#     print(f"fib_idx = {fib_idx}, fib_sum = {fib_sum}")
# if(fib_sum == numb):
#     print(f"fib_idx = {fib_idx+1}") # по примеру +1, в вики с 0 начало
# else:
#     print(f"-1")
# # print(fib_idx if (fib2 == numb) else "-1")
# a = int(input("Введите число а: "))
# f1 = 1
# f2 = 1
# temp = 0
# index = 3

# while f2 < a:
#     temp = f1
#     f1 = f2
#     f2 = f2 + temp

#     index += 1

# if a == f2:
#     print(index)
# else: print ("-1")

# Решение 2
# n = int(input("Введите число: "))
# i = 1
# a=0
# b=1

# while n>a:
#     temp = a + b
#     a = b
#     b = temp
#     i+=1
# # else:
# if (a==n): 
#     print(f"Номер {i}")
# else:
#     print(f"Номер -1")

# Решение 3

# fibRezalt = 0  # последнее число в ряде фибоначи пока не известное
# fib1= 1    # предпоследнее число 
# fib2= 0     # пред-предпоследнее число
# count = 0
# A = int(input("ВВедите число для определения: ")) # вводимое число

# while fibRezalt <= A:
#     fibRezalt = fib1 + fib2

#     fib2 = fib1
#     fib1 = fibRezalt

#     count = count+1

# if(A==fib2):
#     print(count)
# else:
#     print(-1)

# Решение 4

# n = int(input("Введите число: "))
# f_i = 2
# f_1 = 0
# f_2 = 1

# while f_2 < n:
#     f_1, f_2 = f_2, f_1 + f_2
#     f_i += 1

# if (f_2 == n): 
#     print(f"Номер {f_i}")
# else:

# Задание 3
#  Уставшие от необычно теплой зимы,жители решили узнать,действительно ли это самая длинная оттепель 
# за всю историю наблюдений за погодой.Они обратились к синоптикам,а те, в свою очередь,
# заниялись исследоваеиями статистики за прошлые годы.Их интересует сколько дней делилась
# самая длинная оттепель . 

#

# n = int(input("Введите количество дней: "))
# count = 0
# countMax = 0

# for i in range(n):
#     x = int(input(f"Темепратура {i+1}: "))
#     if x > 0:
#         count += 1
#         if count > countMax:
#             countMax = count
#     else:
#         count = 0
    
# print(f"Самая длинная оттепель {countMax} дней")


# # Решение2
# day = int(input("Введите количество дней: "))
# tempature = list(input("Введите температуры через пробел: ").split(' '))
# countDays = 0
# finalDays = 0
# for i in range(day):
#     a = int(tempature[i])
#     if a > 0:
#         countDays = countDays + 1

#     else:
#         countDays = 0
#     if countDays > finalDays:
#         finalDays = countDays
# print(f"Самая длинная оттепель: {finalDays}")


# range(5) -> 0, 1, 2, 3, 4
# range(5, 10) -> 5, 6, 7, 8, 9
# range(1, 10, 2) -> 1, 3,

# Задание 15 