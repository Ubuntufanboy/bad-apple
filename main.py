from PIL import Image
from os import system

# TODO find way to detect black and white pixels
# TODO Make function to process each frame of bad-apple
print("Loading Bad Apple!!")
text = [] # This is gunna be a huge list!
for i in range(1, 1095):
    frame = ""
    for y in range(36):
        for x in range(142):
            coordnets = x, y
            image = Image.open(f"new{i}.png")
            test = image.getpixel(coordnets)
            if test[0] < 50:
                frame += " "
            else:
                frame += "#"
    text.append(frame)
    if i == 110:
        print("10%")
    elif i == 220:
        print("20%")
    elif i == 330:
        print("30%")
    elif i == 440:
        print("40%")
    elif i == 550:
        print("50%")
    elif i == 660:
        print("60%")
    elif i == 770:
        print("70%")
    elif i == 880:
        print("80%")
    elif i == 990:
        print("90%")
    elif i == 1000:
        print("Almost done!")
    else:
        pass
print("Ready to play!")
from time import sleep
for i in range(10):
    print(10 - i)
    sleep(1)
system("clear")
for i in range(102):
    print("e", end="")
for frame in text:
    print(frame, end="")
    sleep(0.15)