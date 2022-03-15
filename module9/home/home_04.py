# Lesson 4 module 9
# # Task 1
# phrase = input('Введите слово: ')
#
# for sym in phrase:
#     print(sym, end = ' ')

number = int(input('Введите первое число: '))
step = int(input('Введите шаг: '))

summ = 0

print('\nIP-address:', end = ' ')

for count in range(3):
    print(number, end = '.')
    summ += number
    number += step
print(summ)

# Homework
######################################################
# Task 1

