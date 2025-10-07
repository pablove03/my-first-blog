# a = int(input("Введите количество элементов списка: "))
# num=[]
# for i in range(a):
#     number = int(input(f"Введите {i+1}-е число: "))
#     num.append(number)
# print(num)
# b=sum(num)
# print("Общая сумма: ",b)
# d=sum(num)/len(num)
# print("Среднее арифметическое:",d)
# print("Минимальное число:",min(num),"Максимальное число:",max(num))
# v=[n for n in num if n < 0]
# if v:
#     print("В списке есть отрицательные числа:",v)
#     print("Количество отрицательных чисел =",len(v))
# else:
#     print("В списке нету отрицательных")
# num.reverse()
# print("REVERSE:",num)
# e = [n for n in num if n % 2 == 0]
# if e:
#     print("чётные числа:",e)
#     print("количество чётных =",len(e))
# else:
#     print("чётные числа отсутствуют!")
#///
a = input("Введите число: ")
b = sum(int(digit)for digit in a)
print("Сумма цифр:", b)
