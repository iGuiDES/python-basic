# Task 1
count = 10

while count <= 10:
 if count == 0:
   print('Время вышло!')
   break
 else:
   print(count)
   count -= 1

# Task 2
users_input = int(input('Продолжаем работать? 1/0: '))

while True:
  users_input = int(input('Продолжаем работать? 1/0: '))
  if users_input == 0:
    print('Приложение закрывается ...')
    break
print('Работа завершена')

# Task 3
debtor = input('Компютер заблокирован! Вернешь скэйт - скажу код разблокировки: ')

while True:
  if debtor != '0550':
    debtor = input('Компютер заблокирован! Вернешь скэйт - скажу код разблокировки: ')
  else:
    print('Код верный, завершаю работу ...')
    break

  
