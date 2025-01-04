#Stupid calculater 

what=input("Что делаем? (+;-;*;/;round;%):")

# я думал import math поможет, но нет. Он не может уместить сразу много задач в себе. На возведении в степень и проценте пошел сбой.. 


if what in {"+", "-", "*", "/", "**"}:

    a=float(input("введи первое число:"))
    b=float(input("Введи второе число:"))

    if what=="+":
        c=a+b
        print("результат:"+str(c))

    elif what=="-": 
        c=a-b
        print("результат:"+str(c))

    elif what=="*":
        c=a*b
        print("результат:"+str(c))

    elif what=="/":
        c=a/b
        print("хуй:"+str(c))

    elif what=="**":
        c=a**b
        print("результат:"+str(c))

    else:
        print("Неверные вводные")

elif what in {"round", "%"}:

    a=float(input("введи число:"))

    if what=="round":
        print("результат:"+str(round(a)))

    elif what=="%":
        b=float(input("введи процент:"))
        c=round(a/100*b)
        print(f"Процент {b}% от числа {a} будет {c}")
        
    else:
        print("Неверные вводные")

else:
    print("Неверная операция")


