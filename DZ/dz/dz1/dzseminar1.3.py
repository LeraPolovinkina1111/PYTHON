# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.


a = int(input("Введите шестизначное число номер билета: "))
b = 0
c = 0

if (a < 1000000 and a > 99999):
    b = b+(a % 10)
    a = a//10
    b = b+(a % 10)
    a = a//10
    b = b+(a % 10)
    a = a//10
    c = c+(a % 10)
    a = a//10
    c = c+(a % 10)
    a = a//10
    c = c+(a % 10)

    if(b==c):
        print("Ваш билет счастливый!Поздравляю!")
    else:
        print("К сожалению, ваш билет не счастливый.")
else:
    print("Это не шестизначное число!")
