# Fot task lesson
num = int(input('Введите число: '))
for number in range(1, num // 2 + num % 2 + 1):
    number = number * 2 - 1
    print(number, '** 2 = ', number ** 2)

# Task 1
N = int(input('Type number: '))
for number in range(1, N + 1, 2):
    print(number, '** 3 =', number ** 3)

# Task 2
stool = int(input('Type sum stool: '))
total_stool_sum = 0
for number in range(1, stool + 1, 5):
    total_stool_sum += number
    print('Number stool:', number)
print('Sum:', total_stool_sum)

# Task 3
wake_up = int(input('What time did you wake up? '))
total_water = 0
total_calories = 0

for hour in range(wake_up, 23, 3):
    total_water += 1
    print('Покушать в', hour, 'часов')
    calories = int(input('Сколько калорий съел? '))
    total_calories += calories
print('Всего выпито воды:', total_water)
print('Всего съедено калорий: ', total_calories)