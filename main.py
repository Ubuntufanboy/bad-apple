import numpy as np
import os
import time
from silver import Silver
from threading import Thread
from tqdm import tqdm
from pathlib import Path
def process(img: np.ndarray) -> str:
    vals = np.array([0, 50, 100, 150, 200, 255])
    symbs = np.array(list(" +$#&@"))
    positions = np.searchsorted(vals, img.reshape(-1), "right") - 1
    symb_img = symbs[positions].reshape(img.shape)
    return "".join(symb_img.reshape(-1))

from PIL import Image

frames = []

w1 = []
w2 = []
w3 = []
w4 = []

def wk1():
    for i in tqdm(range(1,1000)):
        try:
            with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
                img = img.getdata(0)
                img = np.array(img)
                w1.append(process(img))
        except:
            pass
def wk2():
    for i in range(1000,2000):
        with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
            img = img.getdata(0)
            img = np.array(img)
            w2.append(process(img))
def wk3():
    for i in range(2000,3000):
        with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
            img = img.getdata(0)
            img = np.array(img)
            w3.append(process(img))
def wk4():
    for i in range(3000,3285):
        with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
            img = img.getdata(0)
            img = np.array(img)
            w4.append(process(img))
f = Thread(target=wk1)
u = Thread(target=wk2)
c = Thread(target=wk3)
k = Thread(target=wk4)

print("Checking terminal size! Please do not change to terminal size")
time.sleep(1)

global x
global y
x = os.get_terminal_size().columns
y = os.get_terminal_size().lines

current = os.getcwd()
p = Path(f"{current}/processed/{x}x{y}")
images = Path(f"{current}/converted/{x}x{y}")

if images.exists():
    pass
else:
    print("Hey! looks like you didn't run convert.py for this terminal size!")
skip = False
exists = False

if p.exists():
    exists = True
    
    length = sum(1 for x in p.glob('*') if x.is_file())
    if length >= 3284:
        print("Already exists")
        skip = True
    else:
        print(f"Expected 3285 files. Got {length}")
        print("Too few files in directory")
else:
    print("Directory does not exist")
if skip == False:
    if exists == False:
        os.chdir("processed")
        os.mkdir(f"{x}x{y}")
        os.chdir("..")
    
    f.start()
    u.start()
    c.start()
    k.start()

    while len(w1) < 999 or len(w2) < 999 or len(w3) < 999 or len(w4) < 284:
        pass
    frames = w1 + w2 + w3 + w4

    # Time to write deez to disk
    os.chdir("processed")
    place = f"{x}x{y}"
    os.chdir(place)
    for i, frame in enumerate(frames):
        os.system(f"touch {i}.txt")
        filename = f"{i}.txt"
        with open(filename, 'w') as f:
            f.write(frame)
    Silver.play(f"{current}/badapple.mp3")
    for frame in frames:
        os.system("clear")
        print(frame)
        time.sleep(0.0635)
else:
    os.chdir("processed")
    place = f"{x}x{y}"
    os.chdir(place)
    Silver.play(f"{current}/badapple.mp3")
    for i in range(1,3286):
        filename = str(i) + ".txt"
        with open(filename) as f:
            frame = f.read()
            print(frame)
            time.sleep(0.0625)
