def sum_sub(lis):
    if not lis:
        return 0
    
    if lis[0] % 2 != 0:
        return lis[0] + sum_sub(lis[1:])
    
    else:
        return -lis[0] + sum_sub(lis[1:])

print(sum_sub([99,10,10]))
