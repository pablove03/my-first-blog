# import random
#
#
# class game:
#     def __init__(self,type,size):
#         self.t=type
#         self.s=size
# Dota2=game("стратегия","50 GB")
# print(Dota2.t)
# print(Dota2.s)
# import message
# print(message.hello)
# message.print_message("Hello world")
# number = random.randint(1,248)
# print(number)
#///
# myfile = open("hello2.txt","w")
# with open("hello2.txt", "r",encoding="utf-8") as file:
#     text=file.read()
#     print(text)
#///
import os
from fileinput import filename


def get_words(filename):
    with open (filename,encoding="utf8") as file:
        text=file.read()
    text=text.replace("\n","")
    text=text.replace(",""").replace(".""").replace("?","").replace("!""")
    text=text.lower()
    words.sort()
    return words
def get_words_dict(words):
    words_dict=dict()

    for word in words:
        if word in words_dict:
         words_dict[word]=words_dict[word]+1
    else:
       word_dict[word]=1
    return words_dict
def main():
    filename=input("Введите путь к файлу:")
    if not os.path.exists(filename):
        print("указаный файл не существвует")
    else:
        words=get_words(filename)
        words_dict=get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20),words_dict[word])

if __name__=="__main__":
    main()