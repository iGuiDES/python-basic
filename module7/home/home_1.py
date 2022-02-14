# Task 1
for meters in 100, 90, 95, 87, 102:
  if meters % 3 == 0:
    print(meters, 'Подходит')
  else:
    print(meters, 'Не подходит')

# Task 2
for out_number in 3, 7, 5, 6, 4:
  result_degree_2 = out_number ** 2
  print(result_degree_2)
  result_degree_3 = out_number ** 3
  print(result_degree_3)
  result_degree_4 = out_number ** 4
  print(result_degree_4)

# Task 3
winners = 0
for ticket in 345, 19, 87, 1020, 421, 555, 67, 89, 1, 123, 666, 755, 12456:
  if ticket >= 100 and ticket % 5 == 0:
    print(ticket, '- этот былет выиграшный!')
    winners += 1
  else:
    print('В другой раз повезёт')
print('Выиграшных билетов', winners)