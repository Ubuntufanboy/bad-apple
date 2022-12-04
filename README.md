# Bad-Apple Ascii script.

![Example image](/ss/example2.png)
(Really zoomed out gnome ternimal)


## How does it work?

This script will download the video and download each frame indivisually. Then it will make the image into a smaller size to fit the terminal window. Next main.py takes each frame and processes the image using Pillow. The pixels brightness is returned to process. Next, The code will look at the brightness and add a ASCII charector that represents the brightness. An example of high brightness is "@#&" and an example of low brightness is " .," representing black. All the frames are put into a list called text and then the we loop over the list printing each frame then sleeping for a 15th of a second making it look like 15 fps.

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
 
Step 2: Check terminal size. Check https://github.com/Ubuntufanboy/bad-apple/issues/6 for more details

Step 3: Still not working? Try look at error messege and open a issue in the issue tab.

Step 4: Try re-installing or check for missing packages

Step 5: Something is seriously wrong. Contact the developer and I'll start working on it right away. Open an issue for better workflow

----------------------
TODO:

- Publish version 1.2 ✅
- Add calabration for window size (Maybe even automatically) ✅
- Update old ASCII sequence ✅
- Make a new video showing new code ✅ here: https://www.youtube.com/watch?v=4VntPQx8Gs4

## Contributing

If you want to help this project then you can make a pull request for any idea or error you find in the code.

You can also make an issue in the issue tab for any features you would like to be added to the project.

### Thank you for reading
