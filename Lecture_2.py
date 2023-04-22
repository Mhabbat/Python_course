# кОЛЕКЦИЯ ДАННЫХ.ПРОФИЛИРОВАНИЕ И ОТКЛАДКА.

# list_1 = []      # пустой список
# list_1 = list() #пустой список
#list_1 = [1,2,3,8] # список со значением
# print(list_1)
# print(*list_1) # убрать все скобочки и знаки.Вывести только значение.
# # цикл for
#for i in list_1:
 #   print(i)
#print(len(list_1))
#print(len(list_1[2]))

# list_1 = [1,5]
# print(list_1)
# list_1.append(8) # функция append добавлят значение в конец списка.
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Функция "pop" - удаление последние значение в списке.

# list_1 =[12, 7, -1, 21, 0]
# print(list_1.pop())  #0
# print(list_1)
# print(list_1.pop())  
# print(list_1)
# print(list_1.pop())  
# print(list_1)
# print(list_1.pop())  
# print(list_1)

# list_1 =[12, 7, -1, 21, 0]
# print(list_1.pop(0))  #12
# print(list_1)
# list_1 =[12, 7, -1, 21, 0]
# print(list_1.pop(1))  #7
# print(list_1)

# ДОБАВЛЕНИЕ ЭЛЕМЕНТА НА НУЖНУЮ ПОЗИЦИЮ

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1)

# СРЕЗ СПИСКА
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(list_1[0])
# print(list_1[1])
# print(list_1[-1]) # выводит с конца.(последни элемент)
# print(list_1[:]) # выводит от начала до конца
# print(list_1[:2]) # от начала до 2 индекса
# print(list_1[len(list_1)-2:]) # выводить последни два элемента
# print(list_1[0:len(list_1):6]) # от начало до конца с шагом 6

# КОРТЕЖ - неизменяемый список
# t =()
# print(type(t))

# t = (1)
# print(type(t))

# t = (1,5,3)
# print(type(t))

# v = [1,8,9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v
# print(a, b, c)

# СЛОВАРИ - это неупорядочные коллеции пройзвольных объуктов с доступом ключу
# d ={} # пустой словарь
# d = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'wetrty'
# print(d['q'])

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

# print(dictionary.items())

# МНОЖЕСТВО
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')      # добавить значение
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')  # удалить значение
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }  удалит все элементы из множество
# print(colors) # set()

# ПРИМЕР
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# # 'fronzenset' замароженные множество
# a = {1,8,6}
# b = frozenset(a)
# print(b)

# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.
# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]
# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
# Профилирование и отладка
