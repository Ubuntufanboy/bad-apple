from PIL import Image
from os import system
from silver import Silver

text = []
for i in range(1, 3286): # There are 1095 frames
    filename = f"new{i}.png"
    with Image.open(filename) as image:
       frame = ''.join('#' if pix > 50 else '.' for pix in image.getdata(0))
    text.append(frame)
    if i % 10 == 0:
        print(f"{i}/3285")
print("Ready to play!")
from time import sleep
sleep(1)
system("clear")
for i in range(80):
    print("e", end="")
Silver.play("badapple.mp3")
for frame in text:
    print(frame, end="")
    sleep(0.063)
    system("clear")
Silver.stop()    
