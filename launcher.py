""" Pathlib is used to get info about paths"""
from pathlib import Path
import os

print("Welcome to the Bad-Apple script launcher * Press enter to continue *")
input()

current = os.getcwd()
filepath = f"{current}/img"
p = Path(filepath)

skip = False
print("Verdict:" ,end="")

if p.exists():
    length = sum(1 for x in p.glob('*') if x.is_file())
    if length >= 3284:
        print("Already exists")
        skip = True
    else:
        print(f"Expected 3285 files. Got {length}")
        print("Too few files in directory")
else:
    print("Directory does not exist")
    try:
        os.mkdir("img")
    except Exception as e:
        print("Could not create new directory!")
        print(e)
    print("Directory made!")
if skip is False:
    os.system("python3 framer.py")

converted_filename = f"{current}/converted"
n = Path(converted_filename)
if n.exists() is False:
    os.mkdir("converted")

processed_filename = f"{current}/processed"
n = Path(processed_filename)
if n.exists() is False:
    os.mkdir("processed")

os.system("python3 convert.py")
os.system("python3 main.py")
