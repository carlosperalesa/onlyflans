van hasta el hito 3
correccion detalles esteticos y se implementan los usuarios
se agrega la pagina tablas para hacer mas sencilla la vista de productos
se agrega la autenticacion para ver ciertos productos
se agrega el tercer y cuarto usuario y nuevas tablas

usuarios:   admin admin
            hola hola
            adios adios

source ./venv/Scripts/activate
cd onlyflans
python manage.py runserver

python -m pip freeze > requirements.txt 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver