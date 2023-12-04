#!/bin/bash

# config file test
if [ -e "./app/config/config.py" ]; then
  echo "config.py exist -> continue"
else
  echo "config.py does not exist"
  echo "please create ./app/config/config,py"
  exit 1
fi

# venv test
if [ -d ".venv" ]; then
  # .venv already existed
  echo "venv already existed"
else
  # .venv not exist
  echo "venv does not exist"
  echo "creating venv"
  # create venv
  python3 -m venv .venv
fi

# activate venv
. .venv/bin/activate

# install dependenciess
pip install -r requirements.txt

# run app.py
nohup python3 app/app.py &

done