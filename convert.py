# ./img/output000001.png

from os import system
from PIL import Image
num = 1
# list of all files
print("Hey! This part of the code breaks a lot so listen up! *press enter to continue*")
input()
print("Find the correct size of your terminal. Example sizes are 500x200 or anything like that *press enter to continue*")
input()
print("Once you found your terminal size press enter!")
input()
x = input("How *long* is your terminal window aka. How many charectors fit on one line: ")
y = input("How *tall* is your terminal window aka. How many charectors fit vertically in the window: ")
print("If the program looks weird it's because the values are inncorrect")

def get_file_name(num):
    snum = str(num)
    listed = list(snum)
    if len(listed) != 6:
        amount = 6 - len(listed)
        new = []
        for i in range(amount):
            new.append("0")
        new.append(snum)
        ret = ""
        for number in new:
            ret += number
        return(f"./img/output{ret}.png")

for i in range(1,3286):
    image = Image.open(get_file_name(i))
    image = image.resize((x,y))
    image.save(f'new{i}.png')
