word = input()
res = []
stoat = 0

wrd = list(word)
for i in range(len(wrd)):
    stoat += 1
    if wrd[i].find('f') == False: #ищем букву 'f' в слове
        res.append(stoat-1) #запоминаем индекс буквы

print(res) #вывод списка (со скобками, не бейте ногами...)