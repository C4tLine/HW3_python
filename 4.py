arr = [
    'Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая'
]
enter, stoat = int(input()), 0 #ввод и счётчик

if enter <= 0:
    print("Введите только положительное число или вы живёте вне пространства и времени?") #На всякий случай исключаем отрицательные числа и нуль.

for i in range(enter):
    stoat += 1 #Счётчик
    if stoat > 4: #Исключаем перебор больше 4
        stoat = 0 #Возвращаем нуль
    print(arr[stoat-1]) #Поскольку у списка индекс начинается с нуля, то отнимаем от счётчика один