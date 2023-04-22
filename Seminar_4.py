# 
# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# # Решение 1

# test_list = ("a a a b c a a d c d").split()
# print(type(test_list))
# slovar = {}
# resalt = None
# for i in test_list:
#     if i in slovar:
#         print(f'{i}_{slovar[i]}')
#         slovar[i] += 1
#     else:
#         print(f'{i}')
#         slovar[i] = 1


# # Решение 2

# string = "a a a b c a a d c d d"
# my_list = string.split()
# my_dict = dict()

# for i in range(len(my_list)):
#     if my_list[i] in my_dict.keys():
#         my_dict[my_list[i]] += 1
#         my_list[i] = f"{my_list[i]}_{my_dict[my_list[i]]}"
#     else:
#         my_dict[my_list[i]] = 0
# print(my_list)

# решение 3

# my_str = input("Введите символы через пробел: ").split()
# new_list = []

# for i in range(len(my_str)):
#     n = my_str[0:i].count(my_str[i])
    
#     if n > 0:
#         new_list.append(f'{my_str[i]}_{n}')        

#     else:
#         new_list.append(my_str[i])

# print(*new_list) 

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# решение 1
# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells ").lower()
# print(len(set(text.split())))

# # решение 2

# input_text = """She sells sea shells on the sea shore The shells
#  that she sells are sea shells I'm sure.So if she sells sea
#  shells on the sea shore I'm sure that the shells are sea
#  shore shells"""
# print(len(set(input_text.lower().split())))


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Решение 1

# num = int(input("Введите число: "))
# max_num = num
# while num != 0:
#     num = int(input("Введите число: "))
#     if num > max_num:
#         max_num = num
# print(f"Максимальное число в последовательности: {max_num}")

# Решение 2

# list = []
# number = None
# while number != 0:
#     number = int(input("Введите число: "))
#     list.append(number)
# print(max(list))
 
# МАРЖОВЫЙ ОПЕРАТОР.Пример
# list = []
# while (number:= int(input("Введите число: "))) != 0:
#     list.append(number)
# print(max(list))


