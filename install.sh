virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations usuario
python manage.py migrate
python manage.py test
python manage.py runserver