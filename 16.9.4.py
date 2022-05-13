class Client:
    def __init__(self,first_name, second_name, city , balance ):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"Информация о клиенте {self.first_name} {self.second_name} г. {self.city} {self.balance} he,"
    def get_guest(self):
        return f"Информация о гостях: {self.first_name} {self.second_name} г. {self.city}"
client_1 = Client('Иван','Петров','Москва',50)
client_2 = Client('Пётр','Ветров','Псков',150)
client_3 = Client('Ирина','Петрова','Москва',250)
guest_list = [client_1,client_2,client_3]
for guest in guest_list:
    print(guest.get_guest())
