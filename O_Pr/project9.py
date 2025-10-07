# a = int(input("Введи количество элементов списка: "))
# b = []
# for i in range(a):
#      number = int(input(f"Введите {i+1} число: "))
#      b.append(number)
# print("Список: ",b)
# s = 0
# for i in range(len(b)):
#     s += b[i]
# print("Общая сумма: ",s)
# b2 = []
# for i in range(len(b)):
#     if b [i] % 2 != 0:
#         b2.append(b[i])
# print("Список без чётных чисел: ",b2)
#///
#Определение и подключение модулей
#модуль massage
# hello = "Hello all"
#
#
# def print_message(text):
#     print(f"Message: {text}")
#///
# #модуль main.pu
# import message  # подключаем модуль message
#
# # выводим значение переменной hello
# print(message.hello)  # Hello all
# # обращаемся к функции print_message
# message.print_message("Hello work")  # Message: Hello work
#///
#Подключение функциональности модуля в глобальное пространство имен
# from message import print_message
# from message import hello
#
# # обращаемся к функции print_message из модуля message
# print_message("Hello work")  # Message: Hello work
#
# # обращаемся к переменной hello из модуля message
# print(hello)  # Hello all
#///
number = 1
s = 0
m=input("Введите числа")
while m != 0:
    s+=input(f"number = {m}")
    number += 1
print("Работа программы завершена",s)
