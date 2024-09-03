# # Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# # Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in a:
#     if elem > 5:
#         print(elem)
#
# # второй вариант
# print(list(filter(lambda elem: elem > 5, a)))
#
# # Даны списки:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
#
# result = list(filter(lambda elem: elem in b, a))
# print(result)
#
# # Ниже представлен пример лямбда-функции,  удваивающей вводимое значение.
# double = lambda x: x * 2
# print(double(5))
#
#
# # Эквивалентна:
# def double(x):
#     return x * 2
#
# #Вот пример использования функции filter() для отбора четных чисел из списка.
#
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)
#
# #Ниже пример использования функции map() для удвоения всех элементов списка.
#
# current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(map(lambda x: x*2 , current_list))
# print(new_list)
#
# #Функция reduce() принимает в качестве аргументов функцию и список. Функция вызывается с помощью лямбда-функции
# # и итерируемого объекта  и возвращается новый уменьшенный результат.
# # Так выполняется повторяющаяся операцию над парами итерируемых объектов. Функция reduce() входит в состав модуля functools.
#
# from functools import reduce
#
#
# current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
# summa = reduce((lambda x, y: x + y), current_list)
# print(summa)
#
#
# #В этом примере мы будем использовать лямбда-функцию со списковым включением и лямбда-функцию с циклом for.
# # Мы выведем на экран  таблицу из 10 элементов.
#
# tables = [lambda x = x: x*10 for x in range(1, 11)]
# for table in tables:
#     print(table())
#
# #Например, есть две цифры, и вы должны определить, какая из них представляет наибольшее число.
#
# max_number = lambda a, b: a if a > b else b
# print(max_number(3, 5))
#
# #Лямбда-функции не допускают использования нескольких операторов, однако мы можем создать две лямбда-функции,
# # а затем вызвать вторую лямбда-функцию в качестве параметра для первой функции.
# # Давайте попробуем найти второй по величине элемент, используя лямбду.
#
# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)
#
#
# #Отсортируйте словарь по значению в порядке возрастания и убывания.
# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
# #Сортируем в порядке возрастания:
#
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
#
# #И в порядке убывания:
#
# result_2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
#
#
# #Напишите программу для слияния нескольких словарей в один.
#
#
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
#
# #Объединить их можно вот так:
#
# result_3 = {}
# for d in (dict_a, dict_b, dict_c):
#     result_3.update(d)
#
#
# #Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#
# result_4 = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
#
# #Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
# #Второй аргумент функции int отвечает за указание основания системы счисления:
#
# print(int('ABC', 16))
#
# #Нужно вывести первые n строк треугольника Паскаля.
# # В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.
#
#
# def pascal_triangle(n):
#     row = [1]
#     y = [0]
#     for x in range(max(n, 0)):
#         print(row)
#         row = [left + right for left, right in zip(row + y, y + row)]
#
#
# pascal_triangle(3)
#
#
# #Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#
# def convert(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= 24 * 3600
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     print(f'{days}:{hours}:{minutes}:{seconds}')
#
# convert(1459872)
#
#
# #Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
#
# # values = input('Введите числа через запятую: ')
# # ints_as_strings = values.split(',')
# # ints = map(int, ints_as_strings)
# # lst = list(ints)
# # tup = tuple(lst)
# # print('Список:', lst)
# # print('Кортеж:', tup)
#
#
# #Выведите первый и последний элемент списка.
#
# lst = [1, 2, 3, 4, 5]
# print(f'Первый: {lst[0]}; последний: {lst[-1]}')
#
# #Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# ]
#
# for x in numbers:
#     if x == 237:
#         break
#     elif x % 2 == 0:
#         print(x)
#
# #Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
#
# set_1 = set(['White', 'Black', 'Red'])
# set_2 = set(['Red', 'Green'])
#
# print(set_1 - set_2)
#
# #Сложите цифры целого числа.
#
# def sum_digits(num):
#     digits = [int(d) for d in str(num)]
#     return sum(digits)
#
# print(sum_digits(5245))
#
# #Посчитайте, сколько раз символ встречается в строке.
#
# string = 'Python Software Foundation'
# count_o = string.count('o')
# print(count_o)
#
# #Поменяйте значения переменных местами.
# x = 5
# y = 10
# x, y = y, x
#
# #С помощью анонимной функции извлеките из списка числа, делимые на 15.
#
# nums = [45, 55, 60, 37, 100, 105, 220]
# result = list(filter(lambda x: not x % 15, nums))
# print(result)
#
#
# #Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
# import collections
#
# text = 'lorem ipsum dolor sit amet amet amet'
# words = text.split()
# counter = collections.Counter(words)
# most_common, occurrences = counter.most_common()[0]
#
# longest = max(words, key=len)
#
# print(most_common, longest)
#
#
# # Вывод: без кавычеу sep разделитель строк, в середине можно указать символ который будет между строк
# print ("I like Python", sep=" ")
#
#
# #Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.\
# a = 3
# a += 4
# a += 5
# print(a)
#
#
# #Напишите программу, которая считывает целое число,
# # после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
#
# a = int(input())
# print('Следующее за числом', a, 'число:', a+1)
# print('Для числа', a, 'предыдущее число:', a-1)
#
#
# #Напишите программу, которая считывает целое положительное число xx и выводит на экран последовательность чисел x, 2x, 3x, 4x, 5x,
# # разделённых тремя черточками.
#
# a = int(input())
# print(a, a*2, a*3, a*4, a*5, sep='-'*3)
#
# print('hellow', 'world', sep='!')
# #добавляет знак в конце строки
#
# #выводит на одну строчку
# print('hi', end=" ")
# print('dog')


# print('введи любое число')
# b = int(input())
# print('теперь еще одно')
# d = int(input())
# print('а теперь сложим их', b + d )

#
# #функция pound округляет в большую сторону
#
# flat_number = int(input('введи номер квартиры:'))
# number = (flat_number - 1) // 20 + 1
# print('это номер поъезда ', number)
# number_2 = (flat_number - 1) % 20 // 4 + 1
# print('это номер этажа ', number_2)

# #проверить есть ли это слово в строке
# my_string = 'hi'
# print('hi' in my_string)
# #сделать всю строку капсом
# my_string_2 = 'hi'
# print(my_string_2.upper())
# #наоборот lower
#
# #убрать пробелы strip, только спарва или слева
#
# #replase изменяет символы или строки внутри
# a = "me and i"
# print(a.replace('i', 'you'))
#
#
# #определить количество символов в строке
# b = 'aaaabbbb cc'
# print(b.count('a'))

# # в строку вставить данные
# def test():
#     name = 'A'
#     age = 25
#     print(f"my name is {name}' and 'im' {age}")
#
#
# def test_split():
#     my_string = 'hi Lili'
#     my_list = my_string.split(' ')
#     print(my_list)
#
#
# def test_from_list_to_string():
#     my_list = ["hi, Lili"]
#     new_string = ' '.join(my_list)
#     print(new_string)
#
#
# def test_calc():
#     # for c in range(1, 10):
#     #     for j in range(1, 10):
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for number_1 in numbers:
#         for number_2 in numbers:
#             print(number_1, '*', number_2, '=', number_1 * number_2)
#
#
# def test_multiplication_table_list():
#     table = []
#     for i in range(1, 11):
#         row = []
#         for j in range(1, 11):
#             row.append(i * j)
#         table.append(row)
#
#     for row in table:
#         print(row)


def is_our_universe():
    # Произведение двоек
    product_of_twos = 2 * 2  # 2 * 2 = 4

    # Проверка условия
    if product_of_twos != 4:
        return False
    else:
        return True


# Пример использования функции
result = is_our_universe()
print(result)  # Вывод: True



