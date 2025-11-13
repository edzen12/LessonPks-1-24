# *args - arguments
def add(*args):
    total = 0
    for i in args:
        total+=i
    print(total)
add(4,4,4,3,4,5,6,7,7)

######## **kwargs - keyword arguments
def pets(owner, **kwargs):
    print(owner)
    for k,v in kwargs.items():
        print(k,v)

pets('ALiya', cat='Felix', dog='Bobik', city='Bishkek', age=18)

#### комбинация
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(7703010101,180,90, 'HELLO', True,name='Gena', prof='Cлесарь')
####
class Student:
    def __init__(self, name, **kwargs):
        self.name =name
        self.kwargs= kwargs

    def info(self):
        print(f"name: {self.name}")
        for i,v in self.kwargs.items():
            print(f"{i}:{v}")

s = Student('Oleg', car='Gelik', home='JK Muras', children='Vanya')
s.info()



import re  # регулярные выражения
nums = [] #4,45,567,6789
my_str = 'rgr4fef45ferfe567rgfrgr6789'
numbers = re.findall('[0-9]+', my_str)
for i in numbers:
    nums.append(int(i))
print(nums)
