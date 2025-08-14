fruits=["apple","banana","limon","Orange"]
print(fruits[1])
print(len(fruits))

fruits.append("Cherry")

fruits.pop(0)
fruits.pop()

for f in fruits:
    print(f)


while True:
    num=input("Введите число:")
    if num=="1":
        fruits.append(input("Введите название фрукта:"))
        print("Фрукт добавлен!")
    elif num==2:
        fruits.pop(0)
        print("Первый фрукт удален!")
    elif num=="3":
        fruits.pop()
        print("Последний фрукт удален!")
    elif num=="4":
        print("Фрукты:")
        print("-----")
        for f in fruits:
            print(f)
