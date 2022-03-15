# Homework
# Task 1
password = input('Введите пароль: ')

while password != 'Python1234':
    print('Неверный пароль!')
    password = input('Попробуйте еще раз! ')
print('Пароль верный! Добро пожаловать!')

# Task 1 lesson
badGradeCount = 0

for student in range(5):
    answer = input('Кто написал произведение? ')
    if (answer == 'Пушкин') or (answer == 'пушкин'):
        print('Верно!')
        break
    print('Не правильно - 2!')
    badGradeCount += 1
print('Количество двоек:', badGradeCount)

###############################################################
# Homework 1

total_bad_grade = 0

for student in range(10):
    answer = input('Кто написал произведение? ')

    if (answer == 'Евгений Онегин') or (answer == 'евгений онегин'):
        print('Верно!')
        break

    print('Не правильно! Садись - ДВА!')
    total_bad_grade += 1

print('Сегодня двоешников:', total_bad_grade)

################################################################

# Homework 2

countCompletedTask = 0
for worker in range(20):
    answer_bos = input('Ты выполнил поставленые задачи? ')

    if (answer_bos == 'Да, конечно, сделал') or (answer_bos == 'да, конечно, сделал'):
        print('Хорошо, молодец!')
        break

    print('Плохо, сегодня работаешь до тех пор, пока не выполнишь!')
    countCompletedTask += 1

print('Не добросовестных сотрудников сегодня:', countCompletedTask)

################################################################

# Homework 3

name = input('Как тебя зовут? ')
total_questions = 0

if name != '':
    questions = input(f'{name}, купи слона! ')
    while True:
        questions = input(f'Все говорят, {questions}, a ты купи слона! ')
        total_questions += 1
        if total_questions == 5:
            break
    print('Ладно тебе, это всего лишь дразнилка =)')

