from random import randint, choice
from time import sleep
from math import pow, sqrt,ceil,floor

print(pow(5,2))

print(sqrt(100))

# while True:
#     n=float(input("Введите число:"))
#     print("1. Возведение числа в квадрат")
#     print("2. Округлить число в меньшую сторону")
#     operation =int(input("Выберите операцию:"))

names=["Ainash", "Abbas","Saliha","Arsen","Umar","Sofia"]
nom=input("Номинация: ")
print(nom+": " + choice(names))