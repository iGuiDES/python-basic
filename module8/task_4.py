print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

first_num = int(input('Введите начальное число: '))
end_num = int(input('Введите конечное число: '))
checker = int(input('Число для проверки кратности: '))
sum_number = 0
counter = 0

for number in range(first_num, end_num + 1, 1):
    if number % checker == 0:
        sum_number += number
        counter += 1
print('Среднее арифметическое всех чисел от', first_num, 'до', end_num, 'кратное числу', checker, ' = ', sum_number // counter)
