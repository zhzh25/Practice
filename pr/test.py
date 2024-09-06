a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x > 5:
        print(x)

sp = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

sp2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(filter( lambda x: x in sp2, sp)))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
for m in my_list:
    if m%2 == 0:
        print(m)

# max = lambda a, b: a if a>b else b
# print(max(3, 5 ))

txt = "Привет, Мир"
z = txt.upper()
print(z)

fruits = ["яблоко", "банан", "вишня"]
fruits.append("апельсин")
print(fruits)


print("Да") if 5 > 2 else print("Нет")


dc = ['holy shit', 'shit', 'holly']
z = dc.remove('shit')
print(dc)

fruits = ["яблоко", "банан", "вишня", "апельсин", "киви", "дыня", "манго"]
print(fruits[1:3])

fruits = {"яблоко", "банан", "вишня"}
more_fruits = ["апельсин", "манго", "виноград"]
fruits.update(more_fruits)
print(sorted(fruits))


car = {
    "brand": "Форд",
    "model": "Мустанг",
    "year": 1964 }
car['color'] = 'red'
print(car)

def my_funk (a, b):
    return a + b
print(my_funk(3, 5))

def my_funk (number):
    return number  % 2 == 0
print(my_funk(4))

def my_funk (list):
    return max(list)
my_list = [1, 2, 3]
print(my_funk(my_list))

def my_funk (list1, list2):
    return list1 + list2
print(my_funk('hello ', 'world'))

def my_funk (strk):
    return len(strk)
print(my_funk('1232312312'))


class Car:
    def __init__(self, color, model):
        self.color = color  # Свойство: цвет
        self.model = model  # Свойство: модель

    def drive(self):
        print(f"{self.model} едет!")

# Создаем объект (машину) на основе класса Car
my_car = Car("красный", "Toyota")
my_car.drive()  # Вывод: Toyota едет!


def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # возвращает текущее значение и сохраняет состояние
        count += 1

# Использование генератора
for number in count_up_to(5):
    print(number)

b = 'aaaabbbb cc'
print(b.count('a'))

