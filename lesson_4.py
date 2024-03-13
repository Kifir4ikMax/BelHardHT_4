# Создать два списка произвольного содержания
list_number_1 = list()
list_number_2 = []


# Добавить к каждому списку по одному элементу в конец и в начало.
# Список 1.
list_number_1.insert(0, 1)
print(list_number_1)
list_number_1.append(2)
print(list_number_1)


# Список 2.
list_number_2.insert(0, 'Cat')
print(list_number_2)
list_number_2.append('MARS')
print(list_number_2)


# Расширить первый список вторым.
# Вариант 1.
list_number_1.extend(list_number_2)
print(list_number_1)


# Вариант 2.
list_number_1.pop()
list_number_1.pop()
list_number_1 += list_number_2
print(list_number_1)



