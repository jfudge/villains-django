# Change the values of the following variables to match the needs of
# your project.
# Run the command "sh virtualenv-installer-mac.sh" in Terminal and
# this file will run the necessary commands to install virtualenv for you.
VIRTUALENV_NAME="myvirtualenv"

sudo pip3 install virtualenv --user
sudo pip3 install virtualenvwrapper --user

sudo mkvirtualenv "$VIRTUALENV_NAME"
sudo workon "$VIRTUALENV_NAME"
