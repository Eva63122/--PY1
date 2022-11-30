salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

summa = spend

for i in range(2, months + 1):
    spend = spend * 1.03
    summa += spend

money_capital_result = round((summa - salary * months) // 1)

print(money_capital_result)
