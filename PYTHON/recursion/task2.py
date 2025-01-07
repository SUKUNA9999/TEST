def summation(n):
    if n==1 or n==0:
        return 1
    else:
        return n+(summation(n-1))

n = int(input("Введите число: "))
if 0 <= n <= 50:
    print(summation(n))
else:
    print("Некоректные данные")