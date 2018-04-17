Angular's Tour Of Heroes API
============================

Angular Tour Of Heroes API written with Django Rest Framework

Usage:
------
Clone this repository::
    git clone https://github.com/SyafiqTermizi/heroesapi.git

Install requirements file::
    pip install -r requirements.txt

Do migration::
    ./manage.py migrate

Load heroes data to database::
    ./manage.py loaddata heroes.json

Note:
----
This project is using PostgreSQL. You can change it in the settings.py file