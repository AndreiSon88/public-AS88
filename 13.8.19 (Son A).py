ticket = int(input("Сколько билетов вы хотите приобрести"))

s = 0

for i in range(ticket):
    age = int(input("Укажите возраст  посетителя"))
    if age < 18:
        s+= 0

    elif 18 <= age <= 25:
            s+= 990

    else:

        s+= 1390
if ticket <= 3:
    print("Общая стоимость билетов =",s, "руб")


else:
    print("скидка 10% при покупке больше 3 х билетов",s*0.9 )