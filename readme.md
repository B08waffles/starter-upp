=====================================================================================
        ~Instructions to setup and configure 'starterupp' web service~
=====================================================================================
_____________________________________________________________________________________

                      *INSTRUCTIONS FOR LINUX BASED SYSTEMS*
_____________________________________________________________________________________

1. Check to see if you have the latest version of Python installed by opening up a
terminal window and typing `python`, if successful you will enter a python shell in
the terminal as confirmed by the presence of >>> (Ctrl+z to exit) otherwise you must
download Python with your Operating System's Package Manager like so:
Debian/Ubuntu/Linux Mint:
`sudo apt install python`
Arch based systems:
`sudo pacman -S python`
Fedora Linux:
`sudo dnf install python` or `sudo dnf install python3.11`

Different operating systems may have access to different versions of Python, for our
purposes here all we need is Python version 3 or above, preferably Python 3.10.2.

2. Go to https://github.com/B08waffles/starter-upp and download as a ZIP, extract the
ZIP and open the folder in Visual Studio Code or similar IDE program.

3. Now we must create a virtual environment, so activate a terminal in your IDE and type
`python -m venv env`, you will see a new folder created called 'env', we need this.

4. Open up a terminal within your IDE and type the following command:
`source env/bin/activate` to activate the Python Virtual Environment needed in order
to setup this web service.

This Python Virtual Environment holds all the packages and dependencies necessary
for this web service to run, it works independently of any pre-existing globally
installed packages, as a self contained file system.

5. Now we must install all our package dependencies by typing into the terminal
`pip install -r requirements.txt`.

6. In the same terminal, with our (env), type `python manage.py runserver` to
start the web service. The web service will be accessible by default via
http://127.0.0.1:8000. You should get a similiar terminal readout:

(env) [brandon@b08waffle starter-upp-main]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 03, 2022 - 08:10:55
Django version 4.0.3, using settings 'starterupp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

7. Please refer to the PDF document that came in the same folder as this file
for further information about how to test the web service against the Proj 2
specifications, examples are given as well for clarity.

8. Step 8 is for when you are up to Proj 2 18. Please go to the settings.py file
around line 176, change the value of the 'burst' rate to 100/second and save.
Now make sure the server is running, open a new terminal in your IDE, you may
need to repeat step 4 with a quick `source env/bin/activate` possibly, otherwise
now type `python manage.py test`, this will run 9 Unit tests to satisfy Proj2.18.
For clarity, this step requires you to have two open terminals to excecute.

_____________________________________________________________________________________

                            *INSTRUCTIONS FOR WINDOWS*
_____________________________________________________________________________________

-------------------------------------------------------------------------------------
DISCLAIMER: While the steps below SHOULD work, I was not able to get this web service
working in my own Windows machine, therefore it is of great preference to the author/
developer that this is ran in a Linux environment, as intended. This can be done
within windows by installing a Linux distro as an App/program via WSL or by way of a
Virtual Machine.
-------------------------------------------------------------------------------------

1. Go to https://www.python.org/downloads/release/python-3104/ and select the
appropriate installer for your version of Windows. This will install Python on your
machine so that we may proceed.

2. Go to https://github.com/B08waffles/starter-upp and download as a ZIP, extract the
ZIP and open the folder in Visual Studio Code or similar IDE program.

3. Now we must create a virtual environment, so activate a terminal in your IDE and type
`python -m venv env` or `python3 -m venv env`, you will see a new folder created
called 'env', we need this.

4. In a terminal within your IDE type the following command:
`env\bin\activate` to activate the Python Virtual Environment needed in order
to setup this web service

This Python Virtual Environment holds all the packages and dependencies necessary
for this web service to run, it works independently of any pre-existing globally
installed packages, as a self contained file system.

5. Now we must install all our package dependencies by typing into the terminal
`pip install -r requirements.txt`.

6. In the same terminal, with our (env), type `python manage.py runserver` to
start the web service. The web service will be accessible by default via
http://127.0.0.1:8000. You should get a similiar terminal readout:

(env) [brandon@b08waffle starter-upp-main]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 03, 2022 - 08:10:55
Django version 4.0.3, using settings 'starterupp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

7. Please refer to the PDF document that came in the same folder as this file
for further information about how to test the web service against the Proj 2
specifications, examples are given as well for clarity.

8. Step 8 is for when you are up to Proj 2 18. Please go to the settings.py file
around line 176, change the value of the 'burst' rate to 100/second and save.
Now make sure the server is running, open a new terminal in your IDE, you may
need to repeat step 4 with a quick `source env/bin/activate` possibly, otherwise
now type `python manage.py test`, this will run 9 Unit tests to satisfy Proj2.18.
For clarity, this step requires you to have two open terminals to excecute.



                            THANKS FOR READING!



                        ============================
                        *       Brandon Kane       *
                        *    Student: 458955663    *
                        *Diploma of Web Development*
                        *        TAFE QLD          *
                        ============================

