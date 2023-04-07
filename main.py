import numpy as np
import os
import time
import pygame
from threading import Thread
from tqdm import tqdm
from pathlib import Path
from PIL import Image


def listen_for_pause():
    while 1:
        if os.path.isfile("PAUSE.truconf"):
            os.system("rm PAUSE.truconf")

            global stopped
            stopped = True
            pygame.mixer.music.pause()


def listen_for_unpause():
    while 1:
        if os.path.isfile("UNPAUSE.truconf"):
            os.system("rm UNPAUSE.truconf")

            pygame.mixer.music.unpause()
            global stopped
            stopped = False


def listen_for_disable():
    while 1:
        if os.path.isfile("DISABLE.truconf"):
            os.system("rm DISABLE.truconf")

            pygame.mixer.quit()


def listen_for_move():
    global frame
    while 1:
        if os.path.isfile("MOVE.truconf"):
            with open("MOVE.truconf") as f:
                seconds = f.read()
            os.system("rm MOVE.truconf")
            global now
            now = True

            pygame.mixer.music.play(start=int(seconds))
            frame = int(seconds) * 15


reimu1 = Thread(target=listen_for_pause)
reimu2 = Thread(target=listen_for_unpause)
reimu3 = Thread(target=listen_for_disable)
reimu4 = Thread(target=listen_for_move)


def process(img: np.ndarray) -> str:
    vals = np.array([0, 50, 100, 150, 200, 255])
    symbs = np.array(list(" +$#&@"))
    positions = np.searchsorted(vals, img.reshape(-1), "right") - 1
    symb_img = symbs[positions].reshape(img.shape)
    return "".join(symb_img.reshape(-1))


frames = []

w1 = []
w2 = []
w3 = []
w4 = []


# Worker 1 will only work on a small portion of the frames
def wk1():
    for i in tqdm(range(1, 900)):
        try:
            with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
                img = img.getdata(0)
                img = np.array(img)
                w1.append(process(img))
        except Exception as e:
            print(e)


def wk2():
    for i in range(900, 1800):
        with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
            img = img.getdata(0)
            img = np.array(img)
            w2.append(process(img))


def wk3():
    for i in range(1800, 2700):
        with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
            img = img.getdata(0)
            img = np.array(img)
            w3.append(process(img))


def wk4():
    for i in range(2700, 3285):
        with Image.open(f"{current}/converted/{x}x{y}/new{i}.png") as img:
            img = img.getdata(0)
            img = np.array(img)
            w4.append(process(img))


f = Thread(target=wk1)
u = Thread(target=wk2)
c = Thread(target=wk3)
k = Thread(target=wk4)

print("Are you using GNOME? y/n If you don't know enter n")
answer = input("(y/n)>>> ")
if answer == "y":
    opener = True
else:
    opener = False

print("Checking terminal size! Please do not change to terminal size")
time.sleep(1)

# This gets terminal size because we need to know how big our image will be
x = os.get_terminal_size().columns
y = os.get_terminal_size().lines

current = os.getcwd()
p = Path(f"{current}/processed/{x}x{y}")
images = Path(f"{current}/converted/{x}x{y}")

if images.exists() is False:
    print("Hey! looks like you didn't run convert.py for this terminal size!")
    exit(1)
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
if not skip:
    if not exists:
        os.chdir("processed")
        os.mkdir(f"{x}x{y}")
        os.chdir("..")

    f.start()
    u.start()
    c.start()
    k.start()

    while len(w1) < 899 or len(w2) < 899 or len(w3) < 899 or len(w4) < 584:
        if len(w1) == 100:
            print("TIP: You can pause the video and music with the remote")
            time.sleep(2)
        if len(w1) == 250:
            print("TIP: You can use the remote by typing python3 remote.py")
            time.sleep(2)
        if len(w1) == 400:
            print("To support us you can share this program with others!")
            time.sleep(2)
        if len(w1) == 600:
            print("Don't forget to star the repo!")
            time.sleep(2)
        if len(w1) == 800:
            print("Almost done, thank you for waiting")
            time.sleep(2)
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

    next_call = time.perf_counter()

    os.chdir("..")
    os.chdir("..")

    pygame.mixer.init()
    pygame.mixer.music.load("badapple.mp3")
    pygame.mixer.music.play()

    reimu1.start()
    reimu2.start()
    reimu3.start()
    reimu4.start()

    stopped = False
    frame = 0

    next_call = time.perf_counter()
    now = False
    while 1:
        if stopped:
            next_call = time.perf_counter() + 1/15
            continue
        if time.perf_counter() > next_call or (now is True):
            if now:
                now = False
            next_call += 1/15
            os.system("clear")
            print(frames[frame])
            frame += 1
else:
    # Get in directory
    os.chdir("processed")
    place = f"{x}x{y}"
    os.chdir(place)

    frames = []
    for i in range(1, 3284):
        filename = str(i) + ".txt"
        with open(filename) as f:
            frame = f.read()
            frames.append(frame)

    #  get back to normal dir
    os.chdir("..")
    os.chdir("..")

    if opener:

        os.system("gnome-terminal --command ./remote.sh")

    pygame.mixer.init()
    pygame.mixer.music.load("badapple.mp3")
    pygame.mixer.music.play()

    reimu1.start()
    reimu2.start()
    reimu3.start()
    reimu4.start()

    stopped = False
    frame = 0

    next_call = time.perf_counter()
    now = False
    while 1:
        if stopped:
            next_call = time.perf_counter() + 1/15  # This means that
            #  No matter how long it is paused, the video will print the next
            #  frame a 15th of a second after the video is unpaused
            continue
        if time.perf_counter() > next_call or now:  # if frame requested now
            if now:
                now = False  # to stop the video from hyper speed
            next_call += 1/15
            os.system("clear")
            print(frames[frame])
            frame += 1
