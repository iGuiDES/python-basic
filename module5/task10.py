print('Задача 10. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».

works_hours = int(input('Введите время: '))

if (works_hours >= 8 and works_hours < 10) or (works_hours >= 12 and works_hours < 14) or (works_hours >= 16 and works_hours < 18) or (works_hours >= 20 and works_hours <= 22):
  print('Можно получить поссылку')
else:
  print('Поссылку получить нельзя')