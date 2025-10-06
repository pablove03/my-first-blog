#number = 4
#while number < 5:
#    print(f"number = {number}")
#    number += 1
#print("Работа программы завершена")
#i = 4
#j = 4
#while i < 18:
    #while j < 18:
      #  print(i * j, end="\t")
     #   j += 4
    #print("\n")
    #j = 4
    #i += 4
# from hello import result


#def print_messages():
        # определение локальных функций
        #def say_hello(): print("Hello")

       # def say_goodbye(): print("Good Bye")

        # вызов локальных функций
      #  say_hello()
     #   say_goodbye()


    # Вызов функции print_messages
    #print_messages()

    #def say_hello():
   #     print("Hello")


  #  def say_goodbye():
 #       print("Good Bye")

#    say_hello()
#    say_goodbye()
#def print_person(name = "Tom", age = 18):
#    print(f"Name: {name} Age: {age}")
#print_person()
#print_person("Bob")
#print_person("Sam",37)
# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")
#
# sum(1,2,3,4,5)
# sum(3,4,5,6)
#
#
# def sum(a, b):
#     return a + b
#
#
# result = sum(4, 6)  # result = 0
# print(f"sum(4, 6) = {result}")  # sum(4, 6) = 10
# print(f"sum(3, 5) = {sum(3, 5)}")  # sum(3, 5) = 8
#

# def print_person(name, age):
#     if age > 120 or age < 1:
#         print("Invalid age")
#         return
#     print(f"Name: {name}  Age: {age}")
#
#
# print_person("Tom", 22)
# print_person("Bob", -102)

# def say_hello(): print("Hello")
# def say_goodbye(): print("Good Bye")
#
# message = say_hello
# message()
# message = say_goodbye
# message()
#///
# def sum(a,b): return a+b
# def multiply(a,b): return a*b
# operation = sum
# result = operation(5,6)
# print(result)
# operation=multiply
# print(operation(5,6))
#///
# def do_operation(a,b,operation):
#     result=operation(a,b)
#     print(f"result={result}")
#
# def sum(a,b): return a+b
# def multiply(a,b): return a*b
#
# do_operation(5,4,sum)
# do_operation(5,4,multiply)
#///
# def sum(a,b): return a+b
# def subtract(a,b): return a-b
# def multiply(a,b): return a*b
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return subtract
#     else:
#         return multiply
#
# operation=select_operation(1)
# print(operation(10,6))
#
# operation=select_operation(2)
# print(operation(10,6))
#
# operation=select_operation(3)
# print(operation(10,6))
#///
def select_operation(choice):
    if choice==1:
        return lambda a,b:a+b
    elif choice==2:
        return lambda a,b:a-b
    else:
        return lambda a,b:a*b

operation=select_operation(1)
print(operation(10,6))

operation=select_operation(2)
print(operation(10,6))

operation=select_operation(3)
print(operation(10,6))
#///
