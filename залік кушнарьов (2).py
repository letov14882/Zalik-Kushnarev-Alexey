#Дано текстовий файл, що вміщає довільний текст.
#Необхідно розробити застосунок, що виведе кількість слів і символів для
#кожного рядку тексту з текстового файлу.
from tkinter import Tk
from tkinter.filedialog import askopenfile

def readtext():
    abc = askopenfile()
    abc1 = abc.readlines()
    return abc1
text = readtext()
textstr = ''.join(text)

print("Ваш текст:")
print(textstr)
print("")


print("Кількість символів у рядках тексту:")
for line in text:
    print(len(line.rstrip('\n').replace(" ", "")))
   
print("")
a =''
b=''
print("Кількість слів у рядках тексту")
for word in text:
    a =str((len(word.split(' '))))
    b = str(a.rstrip('\n'))
    print(str(b))
