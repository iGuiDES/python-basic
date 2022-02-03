# Task 2
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))

if (first_num > second_num) and (first_num > third_num):
  print('Первое число имеет максимальное значение')
elif (second_num > first_num) and (second_num > third_num):
  print('Второе число имеет максимальное значение')
else:
  print('Третье число имеет максимальное значение') 