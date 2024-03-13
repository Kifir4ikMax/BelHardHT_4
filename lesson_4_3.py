# Работа с Дзен Python.
# Извлечём текст из модуля "this"
import this
text = "".join([this.d.get(c, c) for c in this.s])


# Считаем количество строк в Дзен
strings_number = 1
for char in text:
    if char == '\n':
        strings_number += 1
print(strings_number)


# Считаем количество вхождений ключевых слов "is", "and" и "or".
count_is = text.count("is")
count_and = text.count("and")
count_or = text.count("or")
print(count_is, count_and, count_or)


# Складываем в словарь
zen_count = {}
zen_count["is"] = count_is
zen_count["and"] = count_and
zen_count["or"] = count_or
print(zen_count)


# Меняем в Дзен все "is" на "is not"
mutated_text = text.replace('is', 'is not')
print(mutated_text)

