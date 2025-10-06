# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# if a > b:
#     print("Первое число больше")
# elif a == b:
#     print("Числа равны")
# else:
#     print("Второе число больше")
#///
# name = input("Введите ваше имя: ")
# b = input("Введите вашу фамилию: ")
# print("Вас зовут", name , b)
#///
# for n in range(1,21):
#    name = input("Введите вашу фамилию: ")
#///
# for n in range(7,22):
#     print(n)
#///
# for n in range(0,51,2):
#     print(n,end=" ")
#///
# for a in range(50):
#   if a % 2==0:
#         print(a)
#///
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# for a in range(a,b):
#     if a % 2 == 0:
#        print(a,end=" ")
#///
# a = int(input("Введите число: "))
# if a % 2 == 0:
#     print(a,"Число чётное ")
# else:
#     print("Число не чётное")
#///
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a > b > c:
    print("Первое число больше")
elif a < b > c:
    print("Второе число больше")
else:
    print("Третье число больше")