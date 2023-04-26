# Задача №39
# Даны два массива чисел.
# Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива.

# Ввод
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# Вывод:
# 3 3 2 12

# def list_create_random(begin_num, end_num, length):
#     import random
#     return [random.randint(begin_num, end_num) for _ in range(length)]

# def diff_lists(list_1, list_2):
#     for i in range(len(list_1)):
#         if list_2.count(list_1[i]) == 0:
#             print(list_1[i], end=' ')

# len_1st_list = int(input('Enter a number-length for 1st list: '))
# list_1st = list_create_random(1, 9, len_1st_list)

# len_2nd_list = int(input('Enter a number-length for 2nd list: '))
# list_2nd = list_create_random(1, 9, len_2nd_list)

# print(*list_1st)
# print(*list_2nd)

# diff_lists(list_1st, list_2nd)

# Задача №41
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

def list_create_random(begin_num, end_num, length):
    import random
    return [random.randint(begin_num, end_num) for _ in range(length)]


def count_min_neigh_values(list):
    count = 0
    for i in range(1, len((list)) - 1):
        if list[i] > list[i - 1] and list[i] > list[i + 1]:
            count += 1
    return count

len_list = int(input('Enter a number-length for list: '))
list_1st = list_create_random(1, 9, len_list)
print(*list_1st)
print(count_min_neigh_values(list_1st))

# Задача №43
# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:
# 1 2 3 2 3

# Вывод:
# 2

# def list_create_random(begin_num, end_num, length):
#     import random
#     return [random.randint(begin_num, end_num) for _ in range(length)]

# def count_couple(number):
#     # if number == 2:
#     #     return 1
#     # elif number < 2:
#     #     return 0
#     # else:
#     #     return count_couple(number - 1) + (number - 1)
#     if number < 2:
#         return 0
#     else:
#         return 1 if number == 2 else count_couple(number - 1) + (number - 1)


# Задача №45
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1,
# но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10**5.
# Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).

# Ввод: 300

# Вывод: 220 284

def dict_create(end_range):
    dict = {}
    for i in range(2, end_range + 1):
        summ_i = 0
        for j in range(1, (i // 2) + 1):
            summ_i = summ_i + j if i % j == 0 else summ_i
        dict[i] = summ_i
    return dict

def dict_friendly_values(source_dict):
    set_values = set()
    for i in range(2, len(source_dict)):
        for j in source_dict.values():
        # for j in range(len(source_dict)):
            if i == source_dict.get(j) and j == source_dict.get(i) and i != j:
                set_values.add(i)
                set_values.add(j)
    return set_values

number = int(input('Enter a number K: '))
dict = dict_create(number)
print(*dict_friendly_values(dict))

result_list = list(dict_friendly_values(dict))
print(result_list)
for i in range(len(result_list) - 1):
    if result_list[i] < result_list[i + 1]:
        print(result_list[i], result_list[i + 1])