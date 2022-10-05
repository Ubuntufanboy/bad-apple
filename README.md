# Bad-Apple Ascii script.

## How does it work?

This script will download the video and download each frame indivisually. Then it will make the image into a smaller size to fit the terminal window. Next main.py takes each frame and processes the image using Pillow. The pixels brightness is returned to process. Next, The code will check if the brightness is over a predefined level and if so it will add a "#" to the frame string. otherwise it will return a "." representing black. All the frames are put into a list called text and then the we loop over the list printing each frame then sleeping for a 15th of a second making it look like 15 fps.

--------------

## How to use

First, clone the repo ``git clone https://www.github.com/Ubuntufanboy/bad-apple.git``

Second, cd into the repo by running ``cd bad-apple``

Thrid, run this command ``chmod +x install.sh``

Now you can run ``bash ./install.sh``

Next run, ``chmod +x launcher.sh && bash ./launcher.sh``

--------------

# Help! Something isnt working!!

If something isnt working or does not look right here are the tips recomended to fix the issue

Step 1: Check if you have all the important things installed by running these commands ``yt-dlp --help`` and ``ffmpeg --help``.

Step 2: Check terminal size. The window size needed for this program is 142x36. if your terminal window is too big shrink the window size to make it fit. If you cannot do that, edit the file convert.py and change the value 142 to the length of your terminal window and change the width to the width of your terminal window

Step 3: Still not working? Try look at error messege and open a issue in the issue tab.

Step 4: Try re-installing or check for mising packages

Step 5: Something is seriously wrong. Contact the developer and I'll start working on it right away

----------------------

## Contributing

If you want to help this project then you can make a pull request for any idea or error you find in the code.

You can also make an issue in the issue tab for any features you would like to be added to the project.

### Thank you for reading
