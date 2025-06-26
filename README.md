**Here’s a step-by-step guide on how to run a Django project in VS Code after cloning it:**
________________________________________
1. **Clone the Repository (if not done already)**
If you've already cloned the repository, skip to the next step.
1.	Open a terminal and navigate to the directory where you want to clone the project. 
2.	git clone https://github.com/arjelou/prjsystem-locDev/tree/locdev
3.	Change to the cloned project directory: 
4.	cd repository-name
________________________________________
2. **Open the Project in VS Code**
1.	Launch VS Code.
2.	Open the cloned project folder: 
o	Click on File → Open Folder.
o	Select the folder containing the Django project.
________________________________________
3. **Set Up the Python Environment**
1.	Check if Python is Installed:
o	Open a terminal in VS Code and run: 
o	python --version
If Python is not installed, download it from python.org.
2.	Create a Virtual Environment: In the terminal (inside the project directory), run:
3.	python -m venv env
4.	Activate the Virtual Environment:
o	On Windows: 
o	.\env\Scripts\activate
o	On macOS/Linux: 
o	source env/bin/activate
5.	Install Dependencies:
o	Install the project's dependencies from the requirements.txt file: 
o	pip install -r requirements.txt
________________________________________
4. **Configure VS Code for Python**
1.	Install Required Extensions:
o	Open the Extensions view (Ctrl+Shift+X or Cmd+Shift+X on macOS).
o	Install the following extensions: 
	Python (Microsoft)
	Django (Optional, for better Django support)
2.	Select the Python Interpreter:
o	Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the command palette.
o	Type and select Python: Select Interpreter.
o	Choose the Python interpreter from the virtual environment (e.g., .env\Scripts\python.exe or env/bin/python).
________________________________________
5. **Run the Django Project**
1.	Set Up the Database:
o	Apply migrations to set up the database: 
o	python manage.py migrate
2.	Create a Superuser (Optional):
o	If needed, create an admin account: 
o	python manage.py createsuperuser
3.	Run the Django Development Server:
o	Start the server: 
o	python manage.py runserver
4.	Open the Project in the Browser:
o	Visit http://127.0.0.1:8000 to see your project running.
________________________________________
6. **Debug the Django Project in VS Code (Optional)**
1.	Set Up a Debug Configuration:
o	Go to the Debug panel in VS Code (left sidebar).
o	Click the gear icon to create a launch.json file.
o	Add the following configuration: 
o	{
o	  "version": "0.2.0",
o	  "configurations": [
o	    {
o	      "name": "Python: Django",
o	      "type": "python",
o	      "request": "launch",
o	      "program": "${workspaceFolder}/manage.py",
o	      "args": ["runserver"],
o	      "django": true
o	    }
o	  ]
o	}
2.	Start Debugging:
o	Press F5 or click on Run > Start Debugging to run the project in debug mode.
________________________________________
7. **Access the Admin Panel**
1.	Navigate to **http://127.0.0.1:8000/admin.**
2.	Log in using the superuser account credentials you created.
________________________________________
Now your Django project is running in VS Code!

