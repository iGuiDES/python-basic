# Task 1
for degree_three in range(1, 10 + 1):
  print(degree_three ** 3)

# Task 2
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
summ = 0
for summ_number in range(first_num, second_num + 1):
  summ += summ_number
print('Сумма чисел от', first_num, 'до', second_num, 'равна', summ)

# Task 3
wake_up = int(input('Во сколько простнулся? '))
awake_hours = 0
calories_sum = 0
for hour in range(wake_up, 23):
  print('Сейчас', hour, 'часов')
  calories = int(input('Сколько съел за час? '))
  calories_sum += calories
  if calories_sum > 2000:
    print('Хорошо поел, можно и поспать.')
    break
  awake_hours += 1
print('Съедено калорий за день:', calories_sum)
print('Часов не спал:', awake_hours)
