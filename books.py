class BaseBook:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self.__price = price
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value>= 100:
            self.__price = value

    def info(self):
        return f"{self._title} {self._author} {self.price}"
    
class Book(BaseBook):
    def info(self):
        return f"Книга: {self._title} {self._author} {self.price}сом»" 

class EBook(BaseBook):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self._file_size_mb = file_size_mb

    def info(self): 
        return f"Электронная книга: {self._title} — {self._author}, {self.price} сом, файл {self._file_size_mb} МБ"
    
class AudioBook(BaseBook):
    def __init__(self, title, author, price, duration_min):
        super().__init__(title, author, price)
        self._duration_min = duration_min

    def info(self): 
        return f"Электронная книга: {self._title} — {self._author}, {self.price} сом, длительность {self._duration_min} мин»"
    
# Класс Inventory (склад):
# защищённый список _books
# метод add_books(*books): принимает любое количество объектов книг, проверяет тип
# метод find_books(**filters): возвращает список книг, соответствующих переданным параметрам
# метод remove_book(book): удаляет книгу
# метод all_books(): возвращает копию списка книг
# Класс BookStore:
# атрибут name
# объект inventory
# приватный атрибут __income + свойство income (только чтение)
# метод sell_book(title): ищет по названию, удаляет книгу, увеличивает доход
# метод show_status(): возвращает название магазина, доход и список всех книг через info()
# Требования:
# обязательно использовать инкапсуляцию (__ и _), наследование, полиморфизм, *args, **kwargs
# система должна демонстрировать добавление книг, поиск, продажу и отображение состояния магазина

