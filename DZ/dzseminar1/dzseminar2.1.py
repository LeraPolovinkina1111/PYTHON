# На столе лежат n монеток. Некоторые из них
#  лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число
# монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2


m = int(input("Введите колличество монет: "))
countOne = countZero = 0
for i  in range(m):
    count = 0
    coin = int(input("Введите  монеты (0 или 1): "))
    if coin:
        countOne += 1
    else:
        countZero += 1
if countOne > countZero:
    print(countZero)
else:
    print(countOne)