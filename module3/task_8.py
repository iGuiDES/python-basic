print('Задача 8. Режем число на части')

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

number = int(input('Введите четырёхзначное число: '))

number_res_4 = number % 10
number_res_3 = number // 10 % 10
number_res_2 = number // 100 % 10
number_res_1 = number // 1000 % 10

print(number_res_1, number_res_2, number_res_3, number_res_4)