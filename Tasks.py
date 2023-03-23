# 39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# n = int(input('Введите число эл-ов 1го массива: '))
# list1 = [int(input('Введите элемент массива ')) for _ in range(n)]
# print(list1)
# m = int(input('Введите число эл-ов 2го массива: '))
# list2 = [int(input('Введите элемент массива ')) for _ in range(m)]
# print(list2)
# new_list = []
# for num1 in list1:
#     if num1 not in list2:
#         new_list.append(num1)
# print(new_list)
            
        
# 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел

# list1 = [int(input('Введите элемент массива: ')) for _ in range(int(input('Введите число эл-ов массива: ')))]
# print(list1)
# list1_len = len(list1)
# list1 = list1 + list1[:2]
# count = 0
# for i in range(list1_len):
#     if list1[i+1] > list1[i] and list1[i+1] > list1[i+2]:
#         count += 1
# print(count)


# 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# list1 = []
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     list1.append(number)

# count_dict = {}
# count = 0
# for num in list1:
#     if count_dict.get(num):
#         count_dict[num] =+ 1
#     else:
#         count_dict[num] = 1

# for value in count_dict.values():
#     count += value // 2
# print(count)


# 45. Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def friendlynumbers(k):
    d = {}
    for i in range(1, k):
        summa = 0
        for j in range(1, k // 2 + 1):
            if j >= i:
                break
            elif i % j == 0:
                summa += j
        if summa < k:
            d[i] = summa
    return d

k = 100000
my_dict = friendlynumbers(k)
my_dict2 = {}
my_dict2 = my_dict
for key, value in my_dict.items():
    for key2, value2 in my_dict2.items():
        if key == value2 and key2 == value and key != key2:
            print(key, key2)
            my_dict[key] = 0



# def sum_div(n):
#     summa = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#            summa += i
#     return summa

# summ_dict = {} # 284: 220,
# k = int(input())
# for number in range(2, k + 1):
#     if number in summ_dict:
#         if sum_div(number) == summ_dict[number]:
#             print(number, summ_dict[number])
#     summ_dict[sum_div(number)] = number