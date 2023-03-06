
# ввод
#     -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# диапазон
#     5
#     15
# вывод
#     [1, 9, 13, 14, 19]

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_1 = list(map(int, input().split()))
num_min = int(input())
num_max = int(input())
# print(list_1)

print([i for i in range(len(list_1)) if num_min <= list_1[i] <= num_max])