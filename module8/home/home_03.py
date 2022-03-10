# Lesson task
# Task 1
s = int(input('Введите кол-во секунд: '))
for sec in range(s, -1, -1):
    print('Микроволновка греет:', sec)
print('Дзынь!')

# Task 2
total_soldiers = int(input('Количество солдат в шеренге? '))
total_rules = int(input('Сколько правил в уставе? '))
push_ups = 0

for soldier in range(total_soldiers, 0, -4):
    soldier_rules = int(input('Солдат, назови кол-во правил в уставе? '))
    if total_rules != soldier_rules:
        print('Неправильно!', 10 * soldier, 'отиманий!')
        push_ups += 10 * soldier
print('Общее кол-во отжиманий:', push_ups)

# Homework
# Task 1
seconds = int(input('Ввыдите кол-во секунд: '))
for sec in range(seconds, 0, -1):
    print('Прошло', sec, 'секунд')
print('Я иду искать!')

# Task 2
total_soldiers = int(input('Количество солдат в шеренге? '))
total_rules = int(input('Сколько правил в уставе? '))
push_ups = 0

if total_soldiers >= 4:
    for soldier in range(total_soldiers - 4, 0, -4):
        soldier_rules = int(input('Солдат, назови кол-во правил в уставе? '))
    if total_rules != soldier_rules:
        print('Неправильно!', 10 * soldier, 'отиманий!')
    print(soldier)
    push_ups += 10 * soldier
else:
    print('Сегодня повезло!')
print('Общее кол-во отжиманий:', push_ups)

# Task 3
s = int(input('Введите кол-во секунд: '))
for sec in range(s, 0 , -2):
    print('Прошло секунд:', sec)
print('Я иду искать!')