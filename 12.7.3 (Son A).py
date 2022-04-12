per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money_str = input("Введите сумму:")
money = float(money_str)
deposit = []

for key in per_cent:
    deposit.append(money*per_cent[key]/100)

print( "Процент по дипозитам = ", deposit)
deposit_max = max(deposit)


print("Максимальная сумма, которую вы можете забрать = ", deposit_max)