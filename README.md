# Assignment1-SOFE4620
Repository to hold SOFE 4620 project template that uses python and windows in a virtual environment. 

# Setup
- [Windows](#windows-setup)
- [Pycharm Setup](#pycharm-ide-setup)
- [Running Project](#run-project)

# Windows Setup
- Install git [if not already installed](https://git-scm.com/download/win)
- Clone project *run in cmd as admin*
```
git clone https://github.com/GitEntity/Assignment1-SOFE4620
```
- Install [Python}(https://www.python.org/downloads/)
- Add Python and Python scripts to path variable, **no spaces**

![path](img/path.PNG)

- Install dependencies *run in cmd as admin in project folder*
- More documentation on [venv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
```
pip install virtualenv virtualenvwrapper
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate
```


# PyCharm IDE Setup
- download and install [PyCharm](https://www.jetbrains.com/pycharm/)
- you can get a free license from JetBrains if you are a [student](https://www.jetbrains.com/student/)
- to add your venv as an interpreter follow these [instructions](https://www.jetbrains.com/help/pycharm/2016.1/adding-existing-virtual-environment.html)

![VENV Interpreter Setup](img/pycharm-venv.png)

# Run Project
- use configurations created in PyCharm for `connect.py'
- to run, click the green arrow button besides the dropdown used for configuration

![Run](img/run.png)

- to debug, click on the green sun icon

![Debug](img/debug.png)
