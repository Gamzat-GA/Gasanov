money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0 #Инициализация месяцев

while money_capital >= 0:
    month_money = money_capital + salary #Каков бюджет в начале месяца
    spend = spend * (1 + increase) #Затраты с учетом ежемесячного роста цен
    money_capital = month_money - spend #Остаток подушки безопасности

    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)