1) Install PyCharm IDE 
- Visit https://www.jetbrains.com/pycharm/download/ to download PyCharm for Windows
- Click on the Download button  
- Follow instructions on website to install 

2)Setup Project
- One installed, open PyCharm and create new project and save wherever you would like 
- Copy the code from the zip file which is called Carta_main.py, and paste that over the auto created main.py
- Once the code is copied over, the user will need to download these libraries:
	os
	pandas as pd
	datetime
	datetime 
	json
	numpy as np
	sys
- Rename the file to Carta_main.py and at the top, click on Run and then Edit configurations
- Make sure the Script path is set to where you saved your project AND includes the Carta_main.py (should look something like C:\Users\Family\PycharmProjects\cartallc\Carta_main.py)
- Under Parameters, user can put any string they want, but can only be ONE string argument
- Python interpreter shall point to the python interpreter for that project (i.e C:\Users\Family\PycharmProjects\cartallc\venv\Scripts\python.exe)
- Working directory shall point to the directory where your project is saved (i.e C:\Users\Family\PycharmProjects\cartallc)
- Once all of that is setup, hit Apply and then Ok on the bottom right


3)Running the Program
- One all setup, in the Pycharm IDE, go to terminal on the bottom left
- Once there, make sure the directory for your (venv) shows up as your topmost folder (i.e C:\Users\Family\PycharmProjects\cartallc)
- In order to run, user must type in py Carta_main.py
	OPTIONAL: User may also input py Carta_main.py 12/28/1996
	          The first parameter is a date and is OPTIONAL. But if user does input date, it MUST be in format of mm/dd/yyyy
		  If no date parameter, the program will use today's date as specified in the rubric
- After that, user will be asked which csv file they want to use. The user must input the full file path location including
  the file name (should look something like C:/Users/Family/OneDrive/Desktop/cartallc.csv)
	IF INVALID: program will terminate
- If file exists and is valid, the program will then ask the user where they want to save 
  the file, and the user must input full file path location (i.e C:/Users/Family/OneDrive/Desktop)
	IF INVALID: program will ask user to input a valid file path location again, until they input a correct file path
- If file path is valid, the program will then ask the user what they would like the output file to be called (i.e test.json)
- If all done correctly, the file output shall be saved to wherever the user prompted and will have the correct json information



Key Design Decisions
I chose to use python because of the Pandas library which includes many functions that make it simpler to do data analysis. 
This library allowed for importing csv files, data aggregation, and outputting json files. 
In terms of my code, I tried my best to follow Bob Martins clean code where functions should be less than 7 lines and
that there should not be any comments in the code explaining what my code does. Because if my code is written well enough
it should explain itself, thus making comment unnecessary. 


Assumptions
I made the assumption the user has some technical experience but not to much, which is why I made the documentation as detailed as possible.


