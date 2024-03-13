# Создать два списка, с одинаковым кол-вом элементов.
from typing import List

digit_list = [11, 1, 1992]
string_list = ['eleven', 'one', 'nineteen ninty two']


# Сделать из этих списков словарь.
# Вариант 1. Цикл.
dict_1 = {}
for i in range(len(digit_list)):
    dict_1[digit_list[i]] = string_list[i]
print(dict_1)


# Вариант 2. ZIP.
dict_1.clear()
dict_1 = dict(zip(digit_list, string_list))
print(dict_1)


