# ./img/output000001.png

from os import system
from PIL import Image
num = 1
# list of all files
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
    image = image.resize((142,36))
    image.save(f'new{i}.png')
