TRIP_COST = 20


class TransportCard:
    def __init__(self, owner, balance = 0):

        self.__owner = owner
        self.__balance = balance

    def get_owner(self):
        return f'Имя: {self.__owner}'

    def get_balance(self):
        return f'Баланс: {self.__balance}'

    def add_money(self, amount):
        if amount <= 0:
            return 'Сумма должна быть больше 0'
        self.__balance += amount
        return f'Баланс пополнен. Текущий баланс: {self.__balance}'

    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            return 'На балансе недостаточно средств'
        self.__balance -= TRIP_COST
        return f'Поездка оплачена. Остаток: {self.__balance}'
      

card1 = TransportCard("Иван")
card2 = TransportCard("Айсулуу")

card1.add_money(10)
card2.add_money(200)  

print(card1.get_owner())    
print(card1.get_balance()) 
print(card2.get_owner())    
print(card2.get_balance()) 
print(card1.pay_for_trip())
print(card1.get_balance())