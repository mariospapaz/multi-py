# multi-py
You literally drag and drop the contents of your python project in the obvious directory that I created and then run my script.
After that you will be guided by my script

Make sure your project starts with a main.py and you have a requirements.txt else the script will exit


Should you trust it? is it production ready? 
if you have an x86_64 cpu computer yes.


What does this tool do for you?
- Installs docker temporary in my repo directory 
- Each image grabs your project
- They install latest PyInstaller and compile for you with the right flags
- You get your game(s)!


Is this software 100% perfect?
- No.
- Why?

This program has errors
- Python devs have not released python docker image for darwin
- Also Python devs have not released for windows/linux a arm64 image

Until then I am sorry but you need a fast internet cause it will install 3GBs of docker images
