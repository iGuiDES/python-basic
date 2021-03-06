print('Задача 9. Плохой циферблат')

# У Саши в грузовике стоит суперсовременный цифровой циферблат для подсчёта пробега,
# но он постоянно глючит и сбрасывается.
# Саша заметил закономерность:
# каждый раз, когда сумма цифр на циферблате превышает число текущего дня,
# циферблат сбрасывается.
 
# Напишите программу,
# которая получает на вход от пользователя два числа: пробег и номер дня (первое — обязательно трёхзначное),
# затем находит сумму цифр первого числа,
# и если эта сумма больше второго числа,
# выводит сообщение: «Сброс», — и сбрасывает пробег до нуля.
# В противном случае выводится: «Сегодня не сломался».
# В конце также выводится сам пробег.

count_num = int(input('Введите первое число (трёхзначное): '))
day_num = int(input('Введите номер дня: '))

a, b, c = count_num // 100 % 10, count_num // 10 % 10, count_num % 10
sum_first_num = a + b + c

if sum_first_num > day_num:
  sum_first_num = 0
  print('Сброс')
else:
  print('Сегодня не сломался')
print('Пробег равен', sum_first_num, 'километров')

