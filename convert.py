from tqdm import tqdm
import os
from PIL import Image
from pathlib import Path
num = 1

print("Checking... Do not resize the window!")
x = os.get_terminal_size().columns
y = os.get_terminal_size().lines

current = os.getcwd()

print("Verdict: ", end="")

skip = False
exists = False

p = Path(f"{current}/converted/{x}x{y}")  # The path that the frames would go

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

print("Done!")
if skip is False:
    if exists is False:
        try:
            os.chdir("converted")
        except Exception as e:
            print("Something went wrong trying to enter converted directory")
            print(e)
        os.mkdir(f"{x}x{y}")
        os.chdir(f"{x}x{y}")
    else:
        os.chdir("converted")
        os.chdir(f"{x}x{y}")
    for i in tqdm(range(1, 3286)):
        image = Image.open(f"{current}/img/{i}.png")
        image = image.resize((x, y), Image.Resampling.NEAREST)
        image.save(f'new{i}.png')
else:
    print("Converted files already exist! Good to go!")
