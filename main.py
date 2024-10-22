first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]

second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)






# Пример 1 - как выглядит объединение функций map and filter

# def by_3(x):
#     return x * 3
#
#
# def is_odd(x):
#     return x % 2
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(by_3, filter(is_odd, my_numbers))
# print(list(result))

# Пример 2 - списковая сборка
# аналог map

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# # result = [x * 3 for x in my_numbers]
# result = [x * 3 for x in my_numbers if x % 2]
# print(result)

# Пример 4 - условия перед циклом

# my_numbers =['A', 1, 4, 'B', 5, 'C', 2, 6]
#
# result = [x if type(x) == str else x * 5 for x in my_numbers]
#
# print(result)

# Пример 5 - можно делать вложенные циклы

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# result = [x * y for x in my_numbers for y in they_numbers]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
# print(result)