# Documentation
create environment: python3/python -m venv env
activate envirenment: source env/bin/activate
clone the repo
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
