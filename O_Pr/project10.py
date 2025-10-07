# class car:
#     def __init__(self,brand,number):
#         self.brand = brand
#         self.number = number
#
#     def bark(self):
#         print(self.brand, "быстро ездит")
#
# BMW = car("M8","kz999ADM|18")
# print(BMW.brand)
# print(BMW.number)
# print()
#///
# class Calculator:
#     def add(self,a,b):
#         return a + b
#     def multiply(self,a,b):
#         return a * b
#     def c(self,a,b):
#         return a - b
#     def d(self,a,b):
#         return a % b
# calc=Calculator()
# print(calc.c(52,42))
# print(calc.multiply(7,8))
#///
# class Rectangle:
#
#     def __init__(self, w, l):
#         self.width = w
#         self.length = l
#
#     def area(self):
#         return self.width * self.length
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
#
# rect1 = Rectangle(10, 10)
# print("rect1 area: ", rect1.area())
# print("rect1 perimeter: ", rect1.perimeter())
#
# rect2 = Rectangle(10, 20)
# print("rect2 area: ", rect2.area())
# print("rect2 perimeter: ", rect2.perimeter())
#///
# class BankAccount:
#
#     def __init__(self, number, sum):
#         self.account_number = number
#         self.balance = sum
#         print(f"Создан счет. Начальный баланс: {sum} единиц")
#
#     def add(self, sum):
#         self.balance = self.balance + sum
#         print(f"На счет зачислено: {sum} единиц")
#
#     def withdraw(self, sum):
#         if self.balance >= sum:
#             self.balance = self.balance - sum
#             print(f"Со счета снято: {sum} единиц")
#         else:
#             print("Недостаточно средств на счете")
#
#
# acc1 = BankAccount("988466577", 2890)
# acc1.add(5000)
# acc1.withdraw(2000)
# acc1.withdraw(3000)
# acc1.withdraw(10000)
#///
class Employee:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} works")


class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def study(self):
        print(f"{self.name} studies")


class WorkingStudent(Employee, Student):
    pass


tom = WorkingStudent("Tom")
tom.work()
tom.study()