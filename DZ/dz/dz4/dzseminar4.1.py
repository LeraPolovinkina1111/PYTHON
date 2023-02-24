# Даны два неупорядоченных набора целых чисел(может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств

# Пример:

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = int(input('введи кол-во элементов первого множества: '))
m = int(input('введи кол-во элементов второго множества: '))
array1 = set(map(int, input(f'введи {n} цифр через пробел: ').split()))
array2 = set(map(int, input(f'введи {m} цифр через пробел: ').split()))
n = len(array1)
m = len(array2)
array3 = array1.intersection(array2)

print(f'список уникальных символов {sorted(array3)}')
