# a = input("Введите пароль: ")
# b = input("Проверка пароля: ")
# if a == b:
#     print("пароль верный")
# else:
#     print("Пароль не верный!")
#///
# a = int(input("Введите число: "))
# for n in range(1,11):
#     print(f"{a}*{n}=",n*a)
#///
# a = int(input("Введите число: "))
# for n in range(1,11):
#     print(f"{a}+{n}=",n+a)
#///
# import random
# secret=random.randint(1,30)
# while True:
#     guess=int(input("Угадай число: "))
#     if guess==secret:
#         print("Верно!Ты угадал")
#         break
#     elif guess<secret:
#         print("Загаданное число больше")
#     else:
#         print("Загаданное число меньше")
#///
# summa = 0
# a = input("Введите слово: ")
# b = input("Введите букву: ")
# count = a.count(b)
# summa += count
# print("Количество букв: ",count)
#///
a = input("Введите слово: ")
a_lower=a.lower()
if a_lower==a_lower[::-1]:
    print("Слово является палиндромом!")
else:
    print("Слово не является палиндромом")
