print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
result = 0
count = 0

if first_number < second_number: 
  for i in range(first_number, second_number + 1):
    if i % 3 == 0:
      result += i
      count += 1
  print(result // count)
else:
  print('Число', first_number, 'не должно быть больше чем', second_number)

