# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника)


n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Введите количество долек которое хотите отломить: "))

if (k==m or k==n):
    print("Yes")
else:
    print("NO")
