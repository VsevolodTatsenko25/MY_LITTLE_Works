all_price = 15
minutes = int(input('Введите количество израсходованных за месяц минут'))
sms = int(input('Введите количество израсходованных за месяц смс'))
price_min = 0
price_sms = 0
all_price += 0.44 + 100 * 0.05
if minutes > 50 and sms > 50:
    price_min += 0.25
    price_sms += 0.15


print(all_price)


