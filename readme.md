# Caffeine
This is a very simple Python3 project that aims to create a reusable template which can run a simple Python background process in the System tray.
It also constitutes a testing ground to improve my skills with the Python language.

## caffeine-project setup!

### Windows OS
Prerequisites: Windows 10 (or higher) with Python v3.12 properly installed, don't forget to add Python to the PATH variable.

Once you have done that, you can clone this repository in your local environment: <br/>
&emsp; $> git clone https://github.com/gpaolino/caffeine.git

In order to run this project, you need to create a virtual environment and populate it with the dependencies listed in requirements.txt <br/>
Run these commands to get started quickly: <br/>
&emsp; $> cd .\caffeine\ <br/>
&emsp; $> python3 -m venv .venv <br/>
&emsp; $> .\\.venv\Scripts\activate <br/>

Optionally upgrade pip package manager: $> python.exe -m pip install --upgrade pip <br/>

&emsp; $> python3 -m pip install -r requirements.txt <br/>

### Linux OS
Prerequisites: Ubuntu 22.04.4 LTS (or higher) with Python v3.10.12 properly installed.

Once you have done that, you can clone this repository in your local environment: <br/>
&emsp; $> git clone https://github.com/gpaolino/caffeine.git

In order to run this project, you need to create a virtual environment and populate it with the dependencies listed in requirements.txt <br/>
Run these commands to get started quickly: <br/>
&emsp; $> cd caffeine/ <br/>
&emsp; $> sudo apt install python3.10-venv <br/>
&emsp; $> python3 -m venv .venv <br/>
&emsp; $> source .venv/bin/activate <br/>
&emsp; $> python3 -m pip install -r requirements.txt <br/>
&emsp; $> sudo apt-get install python3-tk python3-dev <br/>

Make some small changes to the Python script: <br/>
&emsp; Change the shebang line in the Python script as following: #!.venv/bin/python <br/>
&emsp; Rename the Python script as *.py <br/>
&emsp; Make it executable using the command: $> chmod +x caffeine.py <br/>
