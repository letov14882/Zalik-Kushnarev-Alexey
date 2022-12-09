#Дано текстовий файл, що вміщає довільний текст.
#Необхідно розробити застосунок, що виведе кількість слів і символів для
#кожного рядку тексту з текстового файлу.
from tkinter import Tk
from tkinter.filedialog import askopenfile #з графічного модулю імпорт для відкриття вікна

def readtext():
    abc = askopenfile()
    abc1 = abc.readlines()
    return abc1             #фукнція для створення змінної, що відкриває і читає файл
text = readtext()
textstr = ''.join(text)     #перевід змінної з листа до строки

print("Ваш текст:")
print(textstr)
print("")                   #відображення тексту, що обрали


print("Кількість символів у рядках тексту:")
for line in text:
    print(len(line.rstrip('\n').replace(" ", ""))) #відображення символів
   
print("")   
a =''
b=''
print("Кількість слів у рядках тексту")
for word in text:
    a =str((len(word.split(' '))))
    b = str(a.rstrip('\n'))
    print(str(b))                       #відображення кількості слів
