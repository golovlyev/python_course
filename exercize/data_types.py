# coding: utf-8

"""
    Задачи для само проверки
"""

#  1

"""
    Сформировать возрастающий список из четных чисел от 2 до 10 включительно.
"""
int_list = []
for i, val in enumerate(range(11)):
    if (i % 2 == 0) & (i != 0):
        int_list.append(val)
# test
assert int_list == [2, 4, 6, 8, 10]

int_list = [i for i, val in enumerate(range(11)) if val % 2 == 0 and val != 0]
# test
assert int_list == [2, 4, 6, 8, 10]

int_list = [i for i in range(11) if i % 2 == 0 and i != 0]
# test
assert int_list == [2, 4, 6, 8, 10]


#  2

"""
   Сформировать убывающий список из чисел от 10 до 3.
"""

int_list = []
for i, val in enumerate(reversed(range(11))):
    if val >= 3:
        int_list.append(val)
# test
assert int_list == [10, 9, 8, 7, 6, 5, 4, 3]

int_list = [i for i in reversed(range(11)) if i >= 3]
# test
assert int_list == [10, 9, 8, 7, 6, 5, 4, 3]

#  3

"""
   Создать список только с четными элементами от 10 до 2.
   Попробовать comprehension и цикл
"""

int_list = []
for i, val in enumerate(reversed(range(11))):
    if val >= 2 and val % 2 == 0:
        int_list.append(val)
# test
assert int_list == [10, 8, 6, 4, 2]

int_list = [i for i in reversed(range(11)) if i >= 2 and i % 2 == 0]
# test
assert int_list == [10, 8, 6, 4, 2]

#  4

"""
    Сформировать матрицу n x m, состоящую из нулей
    Попробовать comprehension и цикл
"""

n = 9
m = 10
val = 0
matrix = []
for r in range(n):
    matrix.append([])
    for c in range(m):
        matrix[r].append(val)

print("====MATRIX====")
for r in matrix:
    print(r)
print("====MATRIX====")

matrix = [[val for y in range(m)] for r in range(n)]
print("====MATRIX====")
for b in matrix:
    print(b)
print("====MATRIX====")

#  5

"""
    Дан список, вывести максимальный элемент в списке.
"""

max_el = 0
a = [10, 100, 345, 5467, 2, 690]
for i in a:
    if i > max_el:
        max_el = i
print 'MAX number is {0}'.format(max_el)

#  6
"""
    Найти сумму 2/3 + 3/4 + 4/5 +...+ 9/10
"""

a = 2.0
b = 3.0
sum_m = 0.0
while a < 10 and b < 11:
    sum_m += a / b
    a += 1
    b += 1
print 'SUM is {0}'.format(sum_m)

#  7

"""
    Для произвольной строки получить строку с уникальными символами
    на основе исходной
"""

some_str = "aaaabbbbccccddeffff"
result_str = ""
for i in some_str:
    if not result_str.__contains__(i):
        result_str += i
print(result_str)

#  8

"""
    Для произвольной строки найти кол-во вхождений каждого символа
    Попробовать dict
"""

some_str = "faaaxa2bbbcc2xccddefff2ffx"
char_dict = {}
for i in some_str:
    if not char_dict.has_key(i):
        cnt = 0
        for x in some_str:
            if i == x:
                cnt += 1
        char_dict.__setitem__(i, cnt)
print(char_dict)

#  9
"""
    Удалить в строке все цифры.
"""

some_str = "645236hello789 237wor894032ld"
numbers = "0123456789"
result_str = ""
for i in some_str:
    if not numbers.__contains__(i):
        result_str += i
print(result_str)

#  10

"""
    Описать класс, реализующий десятичный счетчик, который может увеличивать
    или уменьшать свое значение на единицу в заданном диапазоне.
    Предусмотреть инициализацию счетчика значениями по умолчанию и
    произвольными значениями.
    Счетчик имеет 3 метода: увеличения, уменьшения и
    возвращающий текущее состояние счетчика.
    Написать программу, демонстрирующую все возможности класса.

"""