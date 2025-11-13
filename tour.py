class Tour:
    def __init__(self, id, price, days):
        self.__id = id
        self.__price = price
        self._is_booked = False
        self._client = None
        self._days = days 
    
    @property
    def id(self):
        return self.__id
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value>=5000:
            self.__price = value
        else:
            print("цена не может быть ниже 5000 сом")


    def book(self, client): #бронирует тур, делает его недоступным
        pass 

    def cancel_booking(self): #отменяет бронь, делает тур доступным
        pass 

    def info(self): 
        pass 

# class Client:
# Атрибуты:
# name — имя клиента;
# balance — баланс клиента.

# Методы:
# pay(amount) — уменьшает баланс, если хватает денег;
# add_balance(amount) — пополнение счёта;
# info() — возвращает строку с именем и балансом.


class Agency:
    def __init__(self, name):
        self.name = name 
        self.tours = [] 
        self._income = 0  #доход агентства
 
# Методы:
# add_tour(tour) — добавляет новый тур;
# show_available_tours() — показывает все свободные туры;
# book_tour(client, tour_id) — бронирует тур для клиента;
# cancel_all_bookings() — отменяет все активные брони;
# show_status() — показывает состояние всех туров и текущую выручку.