# Task 1
temperature = int(input('Сколько градусов на улице? '))
meters = 0

while temperature > 15:
  meters += 20
  temperature -= 2
  if temperature <= 15:
    break
  meters += 10
print('Пройдено метров:', meters)

# Task 2
for_sum_number = int(input('Введите число: '))
value = 0

while for_sum_number != 0:
  result = for_sum_number % 10
  print(result)
  if result == 5:
    print('Обнаружен разрыв')
    break
  value += result
  for_sum_number //= 10
print('Сумма:', value)

# Task 3
initial_rate = int(input('Введите количество денег: '))

while initial_rate < 10000:
  number_dice = int(input('Введите число (от 1-го до 6-ти): '))
  if number_dice == 3:
    print('Вы проиграли всё!')
    initial_rate = 0
    break
  initial_rate += 500
  print('Вы выграли 500 рублей. Ваш балланс =', initial_rate)
  
print('Игра закончена')
  
