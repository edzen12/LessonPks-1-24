# Задача Симуляция компьютерного клуба
# создаём систему для комп клуба, где можно бронировать и оплачивать места.
# Каждый компьютер имеет свою цену за час, статус (свободен/занят), и время, когда его забронировали.
# Клиенты могут садиться за компьютер, играть и оплачивать время.
# Владелец клуба может смотреть выручку и управлять компьютерами.

class Computer:
    def __init__(self, comp_id:int, hourly_rate:float):
        self.__id = comp_id 
        self.__hourly_rate = hourly_rate  # стоимость часа игры
        self._is_busy = False  #занят-True или нет-False
        self._current_client = None # занят ли комп клиентом
        self._start_time = 0 #начало сессии
    
    @property
    def id(self):
        return self.__id
    
    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if new_rate >= 50 and new_rate<=1000:
            self.__hourly_rate = new_rate
    
    def start_session(self, client, hours): #запускает комп делает занятым
        if self._is_busy:
            print("Занят комп")
            return False
        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_busy = True
            self._current_client = client
            self._start_time = hours
            print(f"{client} занял комп {self.id} на {hours}час, за {cost}сом")
        else:
            print(f"Клиента {client.name} не хватает денег")
         
    def end_session(self): #завершает сессию, считает оплату
        if not self._is_busy:
            print("Компьютер не использовался")
            return 0
        self._is_busy = False
        income = self.__hourly_rate*self._start_time
        client_name = self._current_client.name 
        print("Сессия завершена")
        self._current_client = None
        self._start_time = 0
        return income

    def info(self):
        status = 'Занят' if self._is_busy else "Свободен"
        return f"Комп {self.id} {status} {self.__hourly_rate} сом/ч" 

# 2. Client
# Атрибуты: name, balance
# Методы:
# pay(amount) — уменьшает баланс, если хватает денег.
# add_balance(amount) — пополнение счёта.
# info() — информация о клиенте.

# 3. Club
# Атрибуты: name, computers — список объектов Computer
# _income — защищённый атрибут, выручка клуба.
# Методы:
# add_computer(computer)
# find_free_computer()
# serve_client(client, hours) — находит свободный комп, запускает сессию.
# end_all_sessions() — завершает все активные сессии и увеличивает доход клуба.
# show_status() — показывает состояние всех компьютеров и доход.