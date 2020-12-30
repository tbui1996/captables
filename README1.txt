How to setup, configure and run PyCharm Python program 

Assumptions
- Instructions are for Windows 10 platform running the latest version and updates
- User is already familiar with Windows and IDE software development environment
- "username" mentioned below refers to the name of the account currently logon
  (one can identify username by typing "echo %username%" from a command shell)
- ...

Install PyCharm IDE 
- Visit https://www.jetbrains.com/pycharm/download/ to download PyCharm for Windows
- Click on the Download button  
- Install PyCharm by going to Downloads folder and double-clicking on newly downloaded PyCharm*.exe
- Launch PyCharm by typing PyCharm into search box and then selecting PyCharm xxxx to run
- Select File > Settings > Build, Execution, Development > Console > Python Console
- In the "Python interpreter" box, select Project Default from dropdown menu C:\Users\username\PycharmProjects\cartaproject\venv\Scripts\Python.exe
- ...

Unzip THOMAS-BUI-CARTA.zip and extract three files onto your desired folder (e.g. Desktop)

Run Python program
Option 1
Open a command shell by typing cmd into the search box and selecting "Command Prompt"
Change to Python executable directory by entering "cd %userprofile%\PycharmProjects\cartaproject\venv\Scripts"
Execute Python program by entering: "python C:/Users/username/Desktop/carta_main.py"
Follow instructions as prompted

Option 2
Launch PyCharm IDE
Select File > Open etc.... 

Key design decisions
....
