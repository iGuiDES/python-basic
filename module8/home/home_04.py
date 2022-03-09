# Task lesson
# Task 1
begin_number = int(input('Введите начальное число: '))
end_number = int(input('Введите конечное число: '))
step = int(input('Введите шаг: '))

for number in range(begin_number, end_number + 1, step):
    print(number, '** 2 = ', number ** 2)
