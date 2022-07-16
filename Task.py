#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. 
#Позиции вводит пользователь через пробел

n = int(input('Введите число: '))
listt = []
for i in range(-n, n+1):
   listt.append(i)
print(listt)
mult=1

a = list(map(int, input('Введите индексы элементов, которые надо перемножить, через пробел: ').split()))
for i in range(len(a)):
    mult = mult * listt[a[i]]
print(mult)

