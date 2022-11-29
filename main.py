from PIL import Image
from time import sleep
from os import system
from silver import Silver
from threading import Thread

frames = []

w1 = []
w2 = []
w3 = []
w4 = []
def wk1():
    for i in range(1,1000):
        filename = f"new{i}.png"
        with Image.open(filename) as image:
        # 255 = @
        # 200 = &
        # 150 = #
        # 100 = $
        # 50 = +
        # 30 = -
        # 20 = .
        # <20 = " "
            frame = ""
            for pix in image.getdata(0):
                if pix == 255:
                    frame += "@"
                elif pix >= 200:
                    frame += "&"
                elif pix >= 150:
                    frame += "#"
                elif pix >= 100:
                    frame += "$"
                elif pix >= 50:
                    frame += "+"
                elif pix >= 30:
                    frame += "-"
                elif pix >= 20:
                    frame += "."
                else:
                    frame += " "
            w1.append(frame)
def wk2():
    for i in range(1000,2000):
        filename = f"new{i}.png"
        with Image.open(filename) as image:
        # 255 = @
        # 200 = &
        # 150 = #
        # 100 = $
        # 50 = +
        # 30 = -
        # 20 = .
        # <20 = " "
            frame = ""
            for pix in image.getdata(0):
                if pix == 255:
                    frame += "@"
                elif pix >= 200:
                    frame += "&"
                elif pix >= 150:
                    frame += "#"
                elif pix >= 100:
                    frame += "$"
                elif pix >= 50:
                    frame += "+"
                elif pix >= 30:
                    frame += "-"
                elif pix >= 20:
                    frame += "."
                else:
                    frame += " "
            w2.append(frame)
def wk3():
    for i in range(2000,3000):
        filename = f"new{i}.png"
        with Image.open(filename) as image:
        # 255 = @
        # 200 = &
        # 150 = #
        # 100 = $
        # 50 = +
        # 30 = -
        # 20 = .
        # <20 = " "
            frame = ""
            for pix in image.getdata(0):
                if pix == 255:
                    frame += "@"
                elif pix >= 200:
                    frame += "&"
                elif pix >= 150:
                    frame += "#"
                elif pix >= 100:
                    frame += "$"
                elif pix >= 50:
                    frame += "+"
                elif pix >= 30:
                    frame += "-"
                elif pix >= 20:
                    frame += "."
                else:
                    frame += " "
            w3.append(frame)
def wk4():
    for i in range(3000,3286):
        filename = f"new{i}.png"
        with Image.open(filename) as image:
        # 255 = @
        # 200 = &
        # 150 = #
        # 100 = $
        # 50 = +
        # 30 = -
        # 20 = .
        # <20 = " "
            frame = ""
            for pix in image.getdata(0):
                if pix == 255:
                    frame += "@"
                elif pix >= 200:
                    frame += "&"
                elif pix >= 150:
                    frame += "#"
                elif pix >= 100:
                    frame += "$"
                elif pix >= 50:
                    frame += "+"
                elif pix >= 30:
                    frame += "-"
                elif pix >= 20:
                    frame += "."
                else:
                    frame += " "
            w4.append(frame)

# Run our workers
f = Thread(target=wk1)
u = Thread(target=wk2)
c = Thread(target=wk3)
k = Thread(target=wk4)

f.start()
u.start()
c.start()
k.start()

# We need to wait til out workers are finished since they are non-blocking
while len(w1) < 997 or len(w2) < 997 or len(w3) < 997 or len(w4) < 283:
    print(len(w2))
sleep(2)
# ITS MORPHIN TIME
for frame in w1:
    frames.append(frame)
for frame in w2:
    frames.append(frame)
for frame in w3:
    frames.append(frame)
for frame in w4:
    frames.append(frame)
print("playing")
Silver.play("badapple.mp3")
for frame in frames:
    system("clear")
    print(frame)
    sleep(0.062)
