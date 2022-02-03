# Task 1
x = int(input('Введите значение по оси "Х": '))
y = int(input('Введите значение по оси "Y": '))

if x > y:
  print('"X" больше "Y"')
else:
  if x < y:
    print('"X" меньше "Y"')
  else:
    print('"X" равен "Y"')

# # Task 2
personal_money = int(input('Введите сумму для оплаты: '))

if personal_money < 75000:
  print('Не хвататет денег на счету =(')
else: 
  personal_money -= 75000
  print('Курс успешно приобретён!')
  if personal_money < 5000:
    personal_money += 1000
    print('Сделана скидка!')
print('Остаток на счету:', personal_money)
print('Хорошего дня!')

# Task 3
received_money = int(input('Введите количество полученых денег: '))

cheese = 60
ice_cream = 20

if received_money - cheese >= 0:
  received_money -= cheese
  print('На сыр денег хватило!')
  if received_money - ice_cream >= 0:
    print('И на мороженое тоже хватило')
else:
  print('Денег маловато =(')
  print('Мама дала всего лишь:', received_money, 'рублей(рубля). Сыр стоит:', cheese, 'рублей')
