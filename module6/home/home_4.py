# Task 1
text = 'Я - программист!'
count_repit = int(input('Введите число: '))
total = 0
while total < count_repit:
  print(text)
  total += 1

# Task 2
event_alarm = int(input('Сколько раз напомнить? '))
event_repit = 0
while event_repit < event_alarm:
  print('Вы хотели не забыть о чём-то')
  event_repit += 1

# Task 3
bags = int(input('Какое количество мешков? '))
bags_count = 0
total_weight = 0

while bags_count < bags:
  question_weight = int(input('Какой вес этого мешка? '))
  total_weight += question_weight
  bags_count += 1
  print('Перенесли мешков -', bags_count, 'из', bags)
print('Общий вес мешков =', total_weight)
