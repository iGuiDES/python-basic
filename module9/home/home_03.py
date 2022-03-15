# Lesson 3 module 9
phrase = input('Введите фразу! ')

for symbol in phrase:
    print(symbol * 5)
    print('=' * 20)

# Lesson 3 module 9
text = input('Введите текст: ')
first_sym = input('Введите первую букву: ')
second_sym = input('Ввдите вторую букву: ')

first_sym_count = 0
second_sym_count = 0

for symbol in text:
    if symbol == first_sym:
        first_sym_count += 1
    if symbol == second_sym:
        second_sym_count += 1

print('Количество букв', first_sym, '=', first_sym_count)
print('Количество букв', second_sym, '=', second_sym_count)

# Homework

#####################################################################

# Task 1
phrase = input('Введите слово: ')

for symbol in phrase:
    print(symbol)

# Task 2
text = input('Введите текст: ')

for i in text:
    print(i * 3)

# Task 3
textarea = input('Введите текст: ')
sym_uppper = input('Введите символ верхнего регистра: ')
sym_lower = input('Введите символ нижнего регистра: ')

count_sym_upper = 0
count_sym_lower = 0

for i in textarea:
    if i == sym_uppper:
        count_sym_upper += 1
    if i == sym_lower:
        count_sym_lower += 1

print('Больших букв', sym_uppper, '=', count_sym_upper)
print('Маленьких букв', sym_lower, '=', count_sym_lower)