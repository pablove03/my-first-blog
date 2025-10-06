# a = "2"
# b = 3
# c = int(a) + b
# print(c)    # 5
#///
# a = int(15)
# b = int(3.7)
# c = int("4")
# e = int(False)
# f = int(True)
#///

# a = "2.7"
# b = 3
# c = float(a) + b
# print(c)
#///
#str
# a = str(False)
# b = str(True)
# c = str(5)
# d = str(5.7)
# #///
# age = 124
# message = "Age: " + str(age)
# print(message)
#///
#global context
# name = "Daniil"
#
# def say_hi():
#     print("Hello",name)
#
# def say_bye():
#     print("Good bye",name)
#
# say_hi()
# say_bye()
#///
#local context
# def say_hi():
#     name="Sam"
#     surname="Johnson"
#     print("Hello",name,surname)
#
# def say_bye():
#     name = "Tom"
#     print("Good bye",name)
#
# say_hi()
# say_bye()
#///
#Hide variables
# name = "Tom"
# def say_hi():
#     name="Bob"
#     print("Hello",name)
#
# def say_bye():
#     print("Good bye",name)
#
# say_hi()
# say_bye()
#///
#nonlocal
# def outer():
#     n=5
#
#     def inner():
#         print(n)
#
#     inner()
#     print(n)
#
# outer()
#///
#Замыкания
# def outer():
#     n=5
#
#     def inner():
#         nonlocal n
#         n+=1
#         print(n)
#
#     return inner
#
# fn=outer()
# fn()
# fn()
# fn()
#///
#use setting
# def multiply(n):
#     def inner(m): return n*m
#
#     return inner
#
# fn = multiply(5)
# print(fn(5))
# print(fn(6))
# print(fn(7))
#///
#сокращение с помощью лямбд ↕
def multiply(n): return lambda m: n*m

fn=multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))
#///
#Decorators
def select(input_func):
    def output_func():
        print("*************")
        input_func()
        print("*************")
    return output_func

@select
def hello():
    print("Hello Metanit.com")
hello()
#///
#Получение параметров функции в декораторе
def check(input_func):
    def output_func(*args):
        input_func(*args)

    return output_func


@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 38)
#///
#Получение результата функции
# определение функции декоратора
def check(input_func):
    def output_func(*args):
        result = input_func(*args)  # передаем функции значения для параметров
        if result < 0: result = 0  # если результат функции меньше нуля, то возвращаем 0
        return result

    return output_func


# определение оригинальной функции
@check
def sum(a, b):
    return a + b


# вызов оригинальной функции
result1 = sum(10, 20)
print(result1)  # 30

result2 = sum(10, -20)
print(result2)  # 0
#///
#3 call and object
class Person:

    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age  # возраст человека


tom = Person("Tom", 22)

# обращение к атрибутам
# получение значений
print(tom.name)  # Tom
print(tom.age)  # 22
# изменение значения
tom.age = 37
print(tom.age)  # 37
#///
class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")


tom=person("Tom",22)
tom.display_info()

bob=person("Bob",43)
bob.display_info()
#///
#Деструкции
class Person:

    def __init__(self,name):
        self.name=name
        print("Создан человек с именем",self.name)

        def __del__(self):
            print("Удалён человек с именем", self.name)

def create_person():
    tom=Person("Tom")

create_person()
print("Конец программы")
#///
#Объекты и классы упражнение 1
class Rectangle:

    def __init__(self,w,l):