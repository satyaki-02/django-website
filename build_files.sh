#!/bin/bash

echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py --noinput --clear
echo "BUILD END"
