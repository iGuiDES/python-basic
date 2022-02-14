print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

classroom = 10
excellent = 0
good = 0
tee = 0

for i in range(1, classroom + 1):
  questions = int(input('Какую оченку получил? '))
  if questions == 5:
    excellent += 1
  elif questions == 4:
    good += 1
  elif questions == 3:
    tee += 1
if excellent > good and excellent > tee:
  print('Сегодня больше отличников, их -', excellent)
elif good > excellent and good > tee:
  print('Сегодня больше хорошистов, их -', good)
else:
  print('Сегодня больше троешников, их -', tee)
