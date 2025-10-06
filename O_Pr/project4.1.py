# def select(input_func):
#     def output_func():
#         print("*****************")
#         input_func()
#         print("*****************")
#     return output_func
#
# @select
# def hello():
#     print("Hello METANIT.COM")
#
# hello()
#///
# def check(input_func):
#     def output_func(*args):
#         input_func(*args)
#     return output_func
# @check
# def print_person(name,age):
#     print((f"Name: {name} Age: {age}"))
#
# print_person("Tom",38)
#///
# def check(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age < 0: age = 1
#         input_func(name, age)
#
#     return output_func
# @check
# def print_person(name, age):
#     print(f"Name: {name}  Age: {age}")
# print_person("Tom",38)
# print_person("Bob",-5)
#///
# def check(input_func):
#     def output_func(*args):
#         result=input_func(*args)
#         if result < 0: result=0
#         return result
#     return output_func
# @check
# def sum(a,b):
#     return a+b
#
# result1=sum(10,20)
# print(result1)
#
# result2=sum(10,-20)
# print(result2)
#///
#Инкапсуляция, атрибуты и свойства
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def print_person(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom = Person("Tom",39)
tom.Person__name="Человек-паук"
tom.print_person()
