print('Задача 4. Календари')

# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.
 
# Напишите программу,
# которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.

count = 0
while True:
  calendar = int(input('Введите число: '))
  if calendar == 0:
    break
  elif calendar % 2 == 0:
    count += 1
print('Четных дней:', count)
