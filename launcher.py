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
    # get the number of files in img folder
    length = sum(1 for x in p.glob('*') if x.is_file())
    if length >= 3284:
        print("Already exists")
        skip = True
    else:
        print(f"Expected 3285 files. Got {length}")
        print("Too few files in directory")
else:
    print("Directory does not exist")
    os.mkdir("img")
    print("Directory made!")
if skip is False: # If we already have the frames downloaded from the video
    print("Extracting frames from Bad-Apple video!")
    os.system("python3 framer.py")

os.system("python3 convert.py")
os.system("python3 main.py")
