# Task 10 module 8
boys = int(input('Какое кол-во мальчиков идет на концерт? '))
girls = int(input('Какое кол-во девочек идет на концерт? '))

answer = ''

if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения!')

elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girls - k):
        answer += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        answer += 'GBG'
    for gb in range(girls - k):
        answer += 'GB'
print(answer)