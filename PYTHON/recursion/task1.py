def factorial(n):
    if n==0:
        return 1
    else:
        return n*(factorial(n-1))

n = int(input("Введите число: "))
if 0 <= n <= 50:
    print(factorial(n))
else:
    print("Некоректные данные")