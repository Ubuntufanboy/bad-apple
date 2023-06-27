"""
Bad-Apple by Ubuntufanboy
Code at https://github.com/Ubuntufanboy/bad-apple

This code was a side project made by me to play
Bad Apple!! in the terminal. I hope you enjoy!

For any issues feel free to open an issue!
"""
import numpy as np
import os
import time
import pygame
from threading import Thread
from PIL import Image


# This function will run constantly once reimu1.start() is called
def listen_for_pause():
    while 1:
        if os.path.isfile("PAUSE.truconf"):
            os.system("rm PAUSE.truconf")

            global stopped
            stopped = True
            pygame.mixer.music.pause()


# This function is in the same boat as listen_for_pause()
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

            with open("UNPAUSE.truconf", 'w') as f:
                f.write("null")

            pygame.mixer.music.play(start=int(seconds))
            frame = int(seconds) * 15


# These Threads don't run yet. They only run when reimu1.start() is called
reimu1 = Thread(target=listen_for_pause)
reimu2 = Thread(target=listen_for_unpause)
reimu3 = Thread(target=listen_for_disable)
reimu4 = Thread(target=listen_for_move)

def img2ascii(arr):
    arr = np.array(arr, dtype=np.uint8)
    # Create a lookup table for mapping brightness values to characters
    lookup_table = np.empty(256, dtype=np.dtype('U1'))
    lookup_table[:100] = " "
    lookup_table[100:200] = "*"
    lookup_table[200:] = "#"
    # Map brightness values to characters using the lookup table
    char_array = lookup_table[arr]

    return char_array

print("Are you using GNOME? y/n If you don't know enter y")  # To start remote
# A new terminal window for the remote
answer = input("(y/n)>>> ")
if answer != "n":
    opener = True
else:
    opener = False

print("Checking terminal size! Please do not change to terminal size")
time.sleep(.5)  # Gives user time to keep terminal size

# This gets terminal size because we need to know how big our image will be
x = os.get_terminal_size().columns
y = os.get_terminal_size().lines

global stopped
stopped = False
data = []
for i in range(1, 3285):
    with Image.open(f"converted/{x}x{y}/new{i}.png") as img:
        data.append(img.getdata(0))
frames = img2ascii(data)

pygame.mixer.init()
pygame.mixer.music.load("badapple.mp3")
pygame.mixer.music.play()

if opener:
    os.system("gnome-terminal --command ./remote.sh")

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
        print(''.join(frames[frame]))
        frame += 1
