# Task 1
number = int(input('Введите число: '))
while number > 0:
  number = int(input('Введите число еще: '))
  number += number
print(number)

# Task 2
password = int(input('Введите пароль: '))
while password != 235:
  print('Неверный пароль!')
  password = int(input('Попробуйте ещё раз: '))
print('Пароль верный! Добро пожаловать!')

# Task 3
questions = int(input('Сколько отложить денег? '))

while questions < 500000:
  print('Нужно еще копить на новую машину!')
  questions = int(input('Сколько отложить денег в этот раз? '))
print('Поздравляю, можно покупать новую машину =)')