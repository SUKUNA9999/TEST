nums1=[9,2,5,6] 

min=nums1[0] #создаем переменную min, которую мы приравниваем к первому элементу массива
for i in nums1: #перебираем все элементы массива, пока не закончится цикл
    if i>min: #если перебираемый элемент меньше, того что в переменной min, то мы перезаписываем min новое значение
        min=i

print(min) #выводим переменную, когда выходим и цикла (то есть перебрали все цисла), таким образом в конце остается минимальное число


funk=lambda x,y: x*y
res=funk(7,4)
print(res)



