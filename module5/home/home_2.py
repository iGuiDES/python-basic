# Task 1
x = int(input('Введите число "X": '))
y = int(input('Введите число "Y": '))

if x > y:
  print('"X" > "Y"')
elif x < y:
  print('"X" < "Y"')
else: 
  print('"X" == "Y"')

# Task 2
profit = int(input('Введите сумму зароботка: '))
if profit <= 0:
  print('Ошибка: доход не может быть отрицательным!')
elif profit < 10000:
  tax = profit * 13 / 100
  print('Сумма налога (13%) = ', tax)
elif profit < 50000:
  tax = profit * 20 / 100
  print('Сумма налога (20%) = ', tax)
else:
  tax = profit * 30 / 100
  print('Сумма налога (30%) = ', tax)

# Task 3
a = int(input('Первая монета: '))
b = int(input('Вторая монета: '))
c = int(input('Третья монета: '))

if a > b:
  print('Первая монета фальшивая')
elif a < b:
  print('Вторая монета фальшивая')
else: 
  print('Третья монета фальшивая')