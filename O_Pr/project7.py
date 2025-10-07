# a = input("Введите текст: ")
# b = a.count(" ")
# print("Количество пробелов : ",b)
# c = a.replace(" ","_")
# print("Предложение с замененными пробелами: ",c)
#///
# a = input("Введите ваш текст: ")
# while len(a)>0:
#     print(a)
#     a=a[:-1]
#///
# a = input("Введите ваш текст: ")
# for i in range(1,len(a)+1):
#     print((a[:i]))
#///
# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except:
#     print("Преобразование прошло неудачно")
# print("Завершение программы")
#///
# import re
# a = input("Введите что-нибудь: ")
# b = re.findall(r'\d+',a)
# b = list(map(int,b))
# if b:
#     average = sum(b)/len(b)
#     print("Числа: ",b)
#     print("среднее арифметическое: ",average)
# else:
#     print("В тексте нет чисел!!!")
#///
a = input("Введите числа: ").split()
nums = list(map(float(a)))
average = sum(a)/len(a)
print("Среднее арифметическое:",average)