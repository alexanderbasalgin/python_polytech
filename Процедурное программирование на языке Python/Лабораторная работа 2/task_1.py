money_capital = 2300  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
answer = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital - spend + salary >= 0:
    money_capital += salary - spend
    spend *= (1 + increase)
    answer += 1
print("Количество месяцев, которое можно протянуть без долгов:", answer)
