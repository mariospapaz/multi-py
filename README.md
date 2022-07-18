# multi-py
An automated process that exports all necessary executables for releasing your game in all 3 platforms

Should you trust it? is it production ready? 
The answer is it depends.

This project is a normie entry for people who want to simply drag-and-drop their project <br>
and magically get a single executable of their game for GNU/Linux, MacOS Catalina, Windows

How to use this program?
Literally drag and drop the contents of your project to `drag-project-files-here`!
- Main program must be called `main.py`
- You MUST have a requirements.txt inside the project you dragged


What does this tool do for you?
- Installs docker temporary in my repo directory 
- Each image grabs your project
- They install latest PyInstaller and compile for you with the right flags
- You get your game(s)!


Is this software 100% perfect?
- No.
- Why?

This program has errors
- It's not working for ARM CPU users due to lack of the below
- Python Devs need to release arm64, x86 images for minimal-windows, minimal-macos, alpine-linux
- Until the above happens, user will have to download atleast 3GB of images just to do something so simple
- A little things are hardcoded I need to get a x86_64 machine in my hands in order to fix them

In my opinion, give a try to GitHub Actions. 
Servers have faster internet than us and then you can just release your binaries to Releases tab
