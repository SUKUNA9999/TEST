def sum_odd(lis):
    if not lis:
        return 0
    
    if lis[0] % 2 != 0:
        return lis[0] + sum_odd(lis[1:])
    
    else:
        return sum_odd(lis[1:])

print(sum_odd([1,2,3,4]) )

