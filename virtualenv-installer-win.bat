@ECHO OFF
REM Change the values of the following variables to match the needs of
REM your project.
REM Run the command "virtualenv-installer-win.bat" in CMD and
REM this file will run the necessary commands to install virtualenv for you.
SET "virtualenv_name=myvirtualenv"

pip install virtualenv
pip install virtualenvwrapper-win

mkvirtualenv "%virtualenv_name%"
workon "%virtualenv_name%"

ECHO ON
