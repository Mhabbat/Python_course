# Задача.Дан список чисел.Определите,сколько в нем встречается различных чисел.
# input:[1,1,2,0,-1,3,4,4]
# output: 6
# # Решение 1
# num_list = [1,1,2,0,-1,3,4,4]
# print(len(set(num_list)))

# Реение 2
# my_str = 'ettfqet'
# my_str = 'etwetwt'
# print(my_str[3],type(my_str))

# Дана последовательность из N целых чисел и число K.Необходимо сдвинуть всю последовательность
# (сдвиг - сиклический) на К элементов вправо, К - положительные число.
# Input [1,2,3,4,5] k = 3
# Output [4,5,1,2,3]
# Решение 1
'''

my_list = [1, 2, 3, 4, 5]
k = 1
for i in range(k):
    my_list.insert(0, my_list.pop())
print(my_list)

# решение 2
my_list = [1,2,3,4,5,]
k = 2 % len(my_list)

print(my_list[-k:] + my_list[: -k])
'''
# Задача.Напишите программу для печати всех уникальных значений в словаре.
'''
start_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"},{"VII": "S005"},
{" V ": "S009"}, {"VIII": "S007"}]
result_set = set()
for mini_dict in start_dict:
    result_set = result_set.union(set(mini_dict.values()))

print(result_set) '''
my_list =[0, -1, 5, 2, 3]
count = 0
for i in range(1,len(my_list)):
    if my_list[i] > my_list[i - 1]:
        count += 1
print(count) 

