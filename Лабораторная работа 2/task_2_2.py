salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

required_money_capital = 0  # Начальное значение подушки безопасности

for _ in range(months):
    # Если зарплата покрывает текущие расходы, подушка безопасности не меняется
    if salary >= spend:
        pass
    else:
        # Если зарплата не покрывает текущие расходы, подушка безопасности увеличивается
        required_money_capital += spend - salary

    spend *= 1 + increase

# Округление вверх до ближайшего целого числа
required_money_capital = round(required_money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_money_capital)
