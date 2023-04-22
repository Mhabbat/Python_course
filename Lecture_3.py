# Функция
# def sum_number(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# print(sum_number(5))

#  # Функция которые принимает неограниченые количество аргументов.
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# МОДУЛЬНОСТЬ
# a = int(input('Введите число а: '))
# b = int(input("Введите число b:"))
# def max(a, b):
#     if a > b:
#         return a
#     return b
# import modul1

# print(modul1.max1(5,9))

# # Вариант2
# from modul1 import max1
# print(max1(5,9))
 # Если хотим импорт все функци нужно использиват *
# from modul1 import *
# print(max1(10, 4))

# import modul1 as m1 # в программе сократили имия файла modul1 на m1
# print(m1.max1(10, 9))

# РЕКУРСИЯ.ФИБОНАЧИ
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n -1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# АЛГОРИТМ.1 Быстроя сортировка.
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10,5,3]))

# СОРТИРОВКА СЛИЯНИЕ
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,2,3,6,9,8,7,66,4]
merge_sort(list1)
print(list1)
        
        