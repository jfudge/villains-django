@ECHO OFF
REM Change the values of the following variables to match the needs of
REM your project.
REM Then run the command "django-installer-cmd.bat" in Git Bash and
REM this file will run the necessary commands to install Django for you.

SET django_version=3.2.5
SET project_name=mydjangosite
SET app_names=app1 app2 app3

echo.Installing required PIP packages...
echo.Installing PostgreSQL driver...

pip install psycopg2

echo.Installing Django %django_version%...

pip install Django==%django_version%

echo.Installing Pillow...

pip install Pillow

echo.Creating requirements.txt...

pip freeze > requirements.txt

echo.Creating new Django project...

django-admin startproject %project_name%

cd %project_name%

for %%a in (%app_names%) do (
  echo.Creating new app called %%a...

  python manage.py startapp %%a
)

python manage.py runserver

ECHO ON
