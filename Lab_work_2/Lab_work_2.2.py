salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0  # Инициализация подушки безопасности

for _ in range(1):
    monthly_budget = salary - spend

    # При отрицательном бюджете используем подушку
    money_capital -= monthly_budget

for _ in range (9):
    monthly_budget = salary - (spend * (1 + increase))
    spend = spend * (1 + increase)  # Увеличиваем цены для нового цикла

    # При отрицательном бюджете используем подушку
    money_capital -= monthly_budget

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.2f}")
