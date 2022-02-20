# Task 1
# get_number = int(input('Введите число: '))
# for number in range(1, get_number + 1):
#     if number % 2 == 0:
#         print(number, '** 3 =', number ** 3)

# optimize code
get_number = int(input('Enter number: '))
for number in range(1, get_number // 2 + 1):
    number *= 2
    print(number, '** 3 =', number ** 3)

# Task 2
total_hourse = int(input('Type count hour: '))
cells = 1
hourse = 0

for hour in range(1, total_hourse // 3 + 1):
    cells *= 2
    print('Прошло часов:', hour * 3)
    print('Клеток:', cells)
    print('Часов до конца эксперимента:', total_hourse - hour * 3)
    print()
print('Наблюдение завершено!')

# Task 3 (while)
n = int(input('Type number: '))
num = 1
while num <= n:
    print(num, '** 2 =',num ** 2)
    num += 2

# Task 3 (for)
N = int(input('Type number: '))

for number in range(1, N // 2 + 1):
    number = number * 2 - 1
    print(number, '** 2 =', number ** 2)
    