
print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

ticket = int(input('Введите шестизначное число: '))
first_three = ticket % 1000
last_three = ticket // 1000
sum_first_three = 0
sum_last_three = 0

while first_three > 0:
  count_first = first_three % 10
  sum_first_three = sum_first_three + count_first
  first_three = first_three // 10
while last_three > 0:
  count_last = last_three % 10
  sum_last_three = sum_last_three + count_last
  last_three = last_three // 10

if sum_first_three == sum_last_three:
  print('Этот билетик счастливый =)')
else:
  print('Увы, возможно в другой раз повезёт =(')

