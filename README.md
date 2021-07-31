# rebrain-py14
Python #14

How to install and run:

1. git clone https://github.com/ingwiz/rebrain-py14
2. cd rebrain-py14/
3. python3 -m venv .venv
4. source .venv/bin/activate
5. pip3 install -r requirements.txt
6. cd config
7. python3 manage.py makemigrations (Optional)
8. python3 manage.py migrate
9. python3 manage.py createsuperuser (Optional)
10. python3 manage.py runserver
11. enter the following addresses in the browser's address bar
  - http://127.0.0.1:8000/api/servers/add
  - http://127.0.0.1:8000/api/servers/
  - http://127.0.0.1:8000/api/servers/status

To exit from `venv` mode enter `deactivate` command
