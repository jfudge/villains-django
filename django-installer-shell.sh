# Change the values of the following variables to match the needs of
# your project.
# Then run the command "sh django-installer-shell.sh" in Git Bash/Terminal and
# this file will run the necessary commands to install Django for you.
MAC=true
WINDOWS=false
DJANGO_VERSION="3.2.5"
PROJECT_NAME="mydjangosite"
APP_NAMES=("app1" "app2" "app3")

if [ "$MAC" = true ]
then
  echo "Installing required PIP packages..."
  echo "Installing PostgreSQL driver..."

  sudo pip3 install psycopg2

  echo "Installing Django $DJANGO_VERSION..."

  sudo pip3 install Django=="$DJANGO_VERSION"

  echo "Installing Pillow..."

  sudo pip3 install Pillow

  echo "Creating requirements.txt..."

  sudo pip3 freeze > requirements.txt

  echo "Creating new Django project..."

  sudo django-admin startproject "$PROJECT_NAME"

  cd "$PROJECT_NAME"

  for APP in "${APP_NAMES[@]}"
  do
    echo "Creating new app called $APP..."

    sudo python manage.py startapp "$APP"

    echo "Creating urls.py and forms.py files..."

    cd "$APP"

    touch urls.py
    touch forms.py

    cd ../
  done

  sudo python manage.py runserver
fi

if [ "$WINDOWS" = true ]
then
  echo "Installing required PIP packages..."
  echo "Installing PostgreSQL driver..."

  pip install psycopg2

  echo "Installing Django $DJANGO_VERSION..."

  pip install Django=="$DJANGO_VERSION"

  echo "Installing Pillow..."

  pip install Pillow

  echo "Creating requirements.txt..."

  pip freeze > requirements.txt

  echo "Creating new Django project..."

  django-admin startproject "$PROJECT_NAME"

  cd "$PROJECT_NAME"

  for APP in "${APP_NAMES[@]}"
  do
    echo "Creating new app called $APP..."

    python manage.py startapp "$APP"

    echo "Creating urls.py and forms.py files..."

    cd "$APP"

    touch urls.py
    touch forms.py

    cd ../
  done

  python manage.py runserver
fi
