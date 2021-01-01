Key Design Decisions
I chose Python because of the Pandas library which includes many functions that make it simpler to do data analysis.
This library allows for importing csv files, data aggregation, and outputting to json format. I follow Bob Martin’s “Clean Code” methodology where functions are less than 7 lines and no comments explaining what the code does. The descriptive variables and function names should be self-explanatory to any software engineer. 


1) Install PyCharm IDE 
- Visit https://www.jetbrains.com/pycharm/download/ to download PyCharm for Windows/Mac
- Click on the Download button  
- Follow instructions on website to install 

2) Setup Project
- Once Pycharm is installed, open PyCharm and create new project and save the project to your desired location 
- Copy the code from Carta_main.py from the zip file and paste into the auto created main.py
- Once the code is copied over, user will need to install these libraries (for more details, please refer to video in zip file):
	os
	pandas
	datetime 
	json
	numpy 
	sys
- Rename the main.py file to Carta_main.p
- Click on Run > Edit configurations
- Make sure the Script path is set to where you saved your project AND include the Carta_main.py (e.g. C:\Users\{UserName}\PycharmProjects\cartallc\Carta_main.py where UserName is the current logged on user)
- Under Parameters, user can put any string they want but can only be ONE string parameter
- Python interpreter shall point to the python interpreter for that project (e.g C:\Users\{UserName}\PycharmProjects\cartallc\venv\Scripts\python.exe)
- Working directory shall point to the directory where your project is saved (e.g C:\Users\{UserName}\PycharmProjects\cartallc)
- Select Apply and then Ok


3)Running the Program
- In the Pycharm IDE, click on the terminal tab on the bottom left
- Make sure the directory for your terminal reflects the working directory (e.g C:\Users\{UserName}\PycharmProjects\cartallc)
- Enter py Carta_main.py
	OPTIONAL: User may also input an optional date argument (e.g py Carta_main.py 01/01/2018). The argument MUST be in the mm/dd/yyyy format.  If no parameter is entered, the program will use today's date as specified in the rubric
- The user will be asked which csv file they want to use. The user must input the full file path location including the file name (e.g C:/Users/{UserName}/OneDrive/Desktop/cartallc.csv)
- IF user input is INVALID the program will terminate
- If file exists and is valid, the program will ask the user where they want to save the output
  file including the full file path location (e.g C:/Users/{UserName}/OneDrive/Desktop)
- IF INVALID: program will ask user to input a valid file path location again until they input a valid file path
- If file path is valid, the program will then ask the user what they would like the output file to be called (i.e test.json)
- If all done correctly, the file output shall be saved to the location the user entered before in a json format


Assumptions
- The user has minimal technical experience
- The user will input a CSV file that is formatted correctly and has all the correct columns and row values. 
- The user will input a valid date format of mm/dd/yyyy




