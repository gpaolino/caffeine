# Caffeine
This is a very simple Python3 project that aims to create a reusable template which can run a simple Python background process in the System tray.
This program prevents your PC from going to sleep. It also constitutes a testing ground to improve my skills with the Python language.

## caffeine-project setup!

### Windows OS
Prerequisites: Windows 10 (or higher) with Python v3.12 properly installed, don't forget to add Python to the PATH variable. <br/>
You can check the Python version installed running this command: <br/>

    $> py --version

Depending on how the environment variable is set it could be: "py", "python" or "python3" <br/>

Once you have done that, you can clone this repository in your local environment: <br/>

    $> git clone https://github.com/gpaolino/caffeine.git

In order to run this project, you need to create a virtual environment and populate it with the dependencies listed in requirements.txt <br/>
Run these commands to get started quickly: <br/>

    $> cd .\caffeine\
    $> py -m venv .venv
    $> .\\.venv\Scripts\activate

Optionally upgrade pip package manager: 

    $> python.exe -m pip install --upgrade pip

Install all the dependencies:

    $> python -m pip install -r requirements.txt

### Linux OS
Prerequisites: Ubuntu 22.04.4 LTS (or higher) with Python v3.10.12 properly installed. <br/>
You can check the Python version installed running this command: <br/>

    $> python3 --version

Once you have done that, you can clone this repository in your local environment: <br/>

    $> git clone https://github.com/gpaolino/caffeine.git

In order to run this project, you need to create a virtual environment and populate it with the dependencies listed in requirements.txt <br/>
Run these commands to get started quickly: <br/>

    $> cd caffeine/
    $> sudo apt install python3.10-venv
    $> python3 -m venv .venv
    $> source .venv/bin/activate
    $> python3 -m pip install -r requirements.txt
    $> sudo apt-get install python3-tk python3-dev

### Install Caffeine as a Local Package
Navigate to the src directory and install your local package: <br/>

    (.venv)$> cd src/
    (.venv)$> python -m pip install .

Run the program: <br/>

    (.venv)$> python caffeine
or Run in background (Windows): <br/>

    (.venv)$> pythonw caffeine

