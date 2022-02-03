print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))

if first_num > second_num:
  max_num = first_num
else:
  max_num = second_num
if third_num > max_num:
  max_num = third_num

print('Максимальное число =', max_num)




