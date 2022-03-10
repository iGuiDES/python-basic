print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

x = int(input('Введите число "x": '))
unaffiliated = 1
double = 1

for i in range(1, 64, 2):
    double *= (x - (2 ** i - 1))
for unaffiliated in range(2, 65, 2):
    unaffiliated *= (x - 2 ** i - 1)

print('Ответ: ', double / unaffiliated)