def nameFunc():
    print("Работа")

def sum(a=0,b=0):
    print(a+b)

def reg(login,password):
    if login=="" or password=="":
        return "Ошибка! Пожалуйста, введите логин и пароль!"
    if len(password)<8:
        return"Пароль должен быть минимум 8 символов!"
    return "Ваш логин и пароль:"+login+". "+password

print(reg(input("Введите логин:"),input("Введите пароль:")))




