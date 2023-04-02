stoat = 0 #Счётчик
arr = list(map(int, input().split())) #Список

for i in range(len(arr)): #0 до длины списка
    for j in range(i + 1, len(arr)): #0 + 1 до длины списка
            if arr[i] == arr[j]: #Если элементы под индексами равны
                 stoat += 1 #Прибавляем счётчик
print(stoat)
