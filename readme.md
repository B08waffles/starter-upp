# STARTERUUPP

> About Starter-Upp: Starter-Upp is a capitalisation system. Instead of manually using spreadsheets to keep track of things like company ownership and individual contributions, this app intends to automate some of the work here by allowing users to create companies, transactions and for this data to be presented to the end-user in the form of both cards and graphs/charts.

This application primarily consist of the following technologies:
- autopep8==1.6.0
- cryptography==36.0.2
- dj-rest-auth==2.2.4
- django-admin-508==0.2.0
- django-admin-interface==0.19.0
- django-allauth==0.50.0
- django-audit-log==0.7.0
- django-audit-log-middleware==0.0.4
- django-cors-headers==3.11.0
- django-environ==0.8.1
- django-filter==21.1
- django-heroku==0.3.1
- django-ip-logger==1.0.1
- django-jazzmin==2.5.0
- django-otp==1.1.3
- django-request-logger==0.3.2
- django-request-logging==0.7.5
- django-requestlogs==0.3.0
- django-simple-ip-restrict==1.0.40
- djangorestframework-jsonapi==5.0.0
- gunicorn==20.1.0
- openapi-codec==1.3.2
- pip-chill==1.0.1
- qrcode==7.3.1
- redgreenunittest==0.1.1
- simplejson==3.17.6

![Lines of code](https://img.shields.io/tokei/lines/github/B08waffles/starter-upp-django-back-end)
![GitHub repo size](https://img.shields.io/github/repo-size/B08waffles/starter-upp-django-back-end)
![GitHub](https://img.shields.io/github/license/B08waffles/starter-upp-django-back-end)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)
![GitHub top language](https://img.shields.io/github/languages/top/b08waffles/starter-upp-django-back-end)
[![GitHub issues](https://img.shields.io/github/issues/B08waffles/starter-upp-django-back-end)](https://github.com/B08waffles/starter-upp-django-back-end/issues)

> **DISCLAIMER:** This application's whitelists has been changed to be in accordance with the deployed version of both itself and its asscoiated front-end, therefore if one wishes to test this application themselves, the whitelists must be adjusted accordingly by whitelisting "http://localhost" and "127.0.0.1". The whitelists can be found in "settings.py", the path to that is "starter-upp/starterupp/settings.py". Note also that debug mode has been set to false, if you are wanting to test this locally you will also want to adjust in settings.py the debug mode by setting it to true.


----------------
## INSTRUCTIONS FOR LINUX BASED SYSTEMS
---------------
1. Check to see if you have the latest version of Python installed by opening up a
terminal window and typing `python`, if successful you will enter a python shell in
the terminal as confirmed by the presence of `>>>` (Ctrl+z to exit) otherwise you must
download Python with your Operating System's Package Manager like so:

__Debian/Ubuntu/Linux Mint:__
```console
sudo apt install python3
```

__Arch based systems:__
```console
sudo pacman -S python3
```

__Fedora Linux:__
```console
sudo dnf install python3
```

 Different operating systems may have access to different versions of Python, for our purposes here all we need is Python version 3 or above, preferably Python 3.10.2.

2. Go to https://github.com/B08waffles/starter-upp and download as a ZIP, extract the
ZIP and open the folder in Visual Studio Code or similar IDE program.

3. Now we must create a virtual environment, so activate a terminal in your IDE and type
`python -m venv env`, you will see a new folder created called 'env', we need this.

4. Open up a terminal within your IDE and type the following command:
`source env/bin/activate` to activate the Python Virtual Environment needed in order
to setup this web service.

> This Python Virtual Environment holds all the packages and dependencies necessary for this web service to run, it works independently of any pre-existing globally installed packages as it is a self contained file system.

5. Now we must install all our package dependencies by typing into the terminal
`pip install -r requirements.txt`.

6. In the same terminal, with our (env), type `python manage.py runserver` to
start the web service. The web service will be accessible by default via
http://127.0.0.1:8000. You should get a similiar terminal readout:

```(env) [brandon@b08waffle starter-upp-main]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 03, 2022 - 08:10:55
Django version 4.0.3, using settings 'starterupp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
7. Please refer to the PDF document that came in the same folder as this file
for further information about how to test the web service against the Proj 2
specifications, examples are given as well for clarity.

8. Step 8 is for when you are up to Proj 2 18. Please go to the settings.py file
around line 176, change the value of the 'burst' rate to 100/second and save.
Now make sure the server is running, open a new terminal in your IDE, you may
need to repeat step 4 with a quick `source env/bin/activate` possibly, otherwise
now type `python manage.py test`, this will run 9 Unit tests to satisfy Proj2.18.
For clarity, this step requires you to have two open terminals to excecute.
-------------
### ADDITIONAL INFO

If you want to test the endpoints with something like postman or Thunder Client you
will need to login or signup at either http://localhost:8000/login/ or 
http://localhost:8000/signup/ respectively, there you will be given a 'Token" upon
successful request, this token needs to be added into the your request
header like so:
```js
 "Authorization": "Token 2fc012d9a97e2a40ed8adddefa47a328658cd767"
 ```
To clarify, you need to prefix the token value with "Token ", there needs to be a
space between Token and its value. Otherwise you can run:
`python manage.py createsuperuser`, then direct your browser to 
http://localhost:8000/admin/ and sign into there to see all CRUD associated with 
this project. 


-----------------------------
## INSTRUCTIONS FOR WINDOWS
-----------------------------


> **DISCLAIMER:** While the steps below _should_ work, I was not able to get this web service working in my own Windows machine, therefore it is of great preference to the author/ developer that this is ran in a Linux environment, as intended. This can be done within windows by installing a Linux distro as an App/program via WSL or by way of a Virtual Machine.


1. Go to https://www.python.org/downloads/release/python-3104/ and select the
appropriate installer for your version of Windows. This will install Python on your
machine so that we may proceed. You need to install Python 3 or above.

2. Go to https://github.com/B08waffles/starter-upp and download as a ZIP, extract the
ZIP and open the folder in Visual Studio Code or similar IDE program.

3. Now we must create a virtual environment, so activate a terminal in your IDE and type
`python -m venv env` or `python3 -m venv env`, you will see a new folder created
called 'env', we need this.

4. In a terminal within your IDE type the following command:
`env\bin\activate` to activate the Python Virtual Environment needed in order
to setup this web service

> This Python Virtual Environment holds all the packages and dependencies necessary for this web service to run, it works independently of any pre-existing globally installed packages, as a self contained file system.

5. Now we must install all our package dependencies by typing into the terminal
`pip install -r requirements.txt`.

6. In the same terminal, with our (env), type `python manage.py runserver` to
start the web service. The web service will be accessible by default via
http://127.0.0.1:8000. You should get a similiar terminal readout:
```
(env) [brandon@b08waffle starter-upp-main]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 03, 2022 - 08:10:55
Django version 4.0.3, using settings 'starterupp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
7. Please refer to the PDF document that came in the same folder as this file
for further information about how to test the web service against the Proj 2
specifications, examples are given as well for clarity.

8. Step 8 is for when you are up to Proj 2 18. Please go to the settings.py file
around line 176, change the value of the 'burst' rate to 100/second and save.
Now make sure the server is running, open a new terminal in your IDE, you may
need to repeat step 4 with a quick `env\bin\activate` possibly, otherwise
now type `python manage.py test`, this will run 9 Unit tests to satisfy Proj2.18.
For clarity, this step requires you to have two open terminals to excecute.
-------------------
### ADDITIONAL INFO
If you want to test the endpoints with something like postman or Thunder Client you
will need to login or signup at either http://localhost:8000/login/ or 
http://localhost:8000/signup/ respectively, there you will be given a 'Token" upon
successful request, this token needs to be added into the your request
header like so:
```js
 "Authorization": "Token 2fc012d9a97e2a40ed8adddefa47a328658cd767"
 ```
To clarify, you need to prefix the token value with "Token ", there needs to be a
space between Token and its value. Otherwise you can run:
`python manage.py createsuperuser`, then direct your browser to 
http://localhost:8000/admin/ and sign into there to see all CRUD associated with 
this project. 



THANKS FOR READING!


```yaml
============================
       Brandon Kane                
============================
```

