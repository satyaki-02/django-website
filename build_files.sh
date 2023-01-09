echo "BUILD START"
python3.10.7 -m pip install -r requirements.txt
python3.10.7 manage.py --noinput --clear
echo "BUILD END"