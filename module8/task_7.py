print('Задача 7. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Укажите месячную стипендию: '))
expenses = int(input('Укажите месячные затраты: '))
total_sum = 0

for i in range(1, 10 + 1, 1):
    total_sum += (expenses - educational_grant)
    expenses *= 1.03
    print(total_sum)
print('У родителей нужно попросить', total_sum)