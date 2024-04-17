#!/bin/bash
VENV_PATH="/data/data/com.termux/files/home/Skola/4L DBI/vtipy/venv"
APP_PATH="/data/data/com.termux/files/home/Skola/4L DBI/vtipy/mysite"
export FLASK_APP="flask_app.py"
. "$VENV_PATH/bin/activate"
cd "$APP_PATH"
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
