import time
print("Welcome to the Bad Apple remote!")
print("")

print("What would you like to do?")
print("1. Pause the program")
print("2. resume the program")
print("3. disable the music")
print("4. move the playhead to a certain time")
print("5. loop a section of the video")
print("6. exit")


def pause():
    # We will send a PAUSE.truconf
    with open("PAUSE.truconf", 'w') as f:
        f.write("null")


def resume():
    with open("UNPAUSE.truconf", 'w') as f:
        f.write("null")


def disable():
    print("This will FULLY disable the music! In order to start it again you will need to rerun launcher.py!!!")
    check = input("To disable to music type YES in all caps otherwise just press enter >>> ")
    if check != "YES":
        exit()
    with open("DISABLE.truconf", 'w') as f:
        f.write("null")


def move():
    print("What second mark should the playhead move to?\
            (if time in minutes convert to seconds)")
    time = int(input("Time (in seconds) >>> "))

    with open("MOVE.truconf", 'w') as f:
        f.write(f"{time}")


def loop():
    start = int(input("Where should the loop start?? "))
    end = int(input("Where should the loop end?? "))
    times = int(input("How many times should it loop? -1 for infinity "))
    if times != -1:
        for i in range(times):
            with open("MOVE.truconf", 'w') as f:
                f.write(f"{start}")
            time.sleep(end-start)
    if times == -1:
        while 1:
            with open("MOVE.truconf", 'w') as f:
                f.write(f"{start}")
            time.sleep(end-start)

def adios():
    print("See ya")
    exit(0)


my_dict = {"1": pause, "2": resume, "3": disable, "4": move, "5": loop, '6': adios}

while 1:
    remote = input("Remote >>> ")
    my_dict[remote]()
