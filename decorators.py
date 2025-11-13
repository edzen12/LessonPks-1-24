def fh():
    print("Привет ребята")

hello = fh # функция это объект
hello()
# №№№№№№№№
def gromko(text):
    return text.upper()

def tiho(text):
    return text.lower()

def speak(func, x):
    res = func(x)
    return res 

print(speak(gromko, 'как дела гена?'))
print(speak(tiho, 'Хорошо Вася, сам как?'))
# №№№№№№№№№ функцию передаем как параметр, и она работает внутри другой
def inc(x):
    return x*2

def dec(x):
    return x/2

def oper(func, x):
    res = func(x)
    return res 

print(oper(inc, 6))
print(oper(dec, 9))

# №№№№№№№№ декоратор - расширение возможности добавляю новые, но не руша старую
def before_after(func):
    def wrapper():
        print("то что может работать до")
        func()
        print("то что может работать после")
    return wrapper

@before_after # декоратор
def say_hi():
    print("привет друг")

say_hi()

#### @property 
    # getter  
    # setter 
    # deleter
class Teacher:
    def __init__(self, name, phone):
        self.name = name 
        self.__phone = phone  
    
    @property # мы обращаемся к методам как к атрибутам, хотя под капотом все работает как метод
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        print("Сеттер сработал")
        self.__phone = value
    
    @phone.deleter
    def phone(self):
        print("Удалили номер deleter")
        del self.__phone
    
    def info(self):
        return f"{self.name} {self.__phone}"

t = Teacher('Ali', 770770770)
t.phone = 45
print(t.phone)
# del t.phone
print(t.info())
        



