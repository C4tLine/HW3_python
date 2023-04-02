arr = list(map(int, input().split())) #Вводим список
steps = -1 #кол-во сдвигов (отрицательное вправо / положительное влево)

arr = arr[steps:] + arr[:steps] #Сдвигаем вправо весь список
print(arr)