#Stupid calculater 

what=input("Что делаем? (+;-;*;/;округление):")
a=float(input("введи первое число:"))
b=float(input("Введи второе число:"))



# я думал import math поможет, но нет. Он не может уместить сразу много задач в себе. На возведении в степень и проценте пошел сбой.. 



if what=="+":
    c=a+b
    print("результат:"+str(c))

if what=="-": 
    c=a-b
    print("результат:"+str(c))

if what=="*":
    c=a*b
    print("результат:"+str(c))

if what=="/":
    c=a/b
    print("хуй:"+str(c))

elif what=="**":
    c=a**
    print("результат:"+str(c))


else:
    print("Неверная комбинация")


