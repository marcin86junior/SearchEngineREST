SearchEngineREST
================

![alt text](http://marcin86.pythonanywhere.com/static/SearchEngineREST.JPG)

Overview
--------

SearchEngineREST is a website for checking new python package. 
Django/REST technology is used for searching in database and recovery.

Requirements:
-------------

	Python 3.8.x
	Django 3.2.12
	Djangorestframework 3.13.x
	Celery 5.1.2
	Redis 3.5.3

Docker:
-------

	Create new folder "SearchEngineREST" and open it:
	git clone https://github.com/marcin86junior/SearchEngineREST.git .
	"CRLF->LF" in \mysite\docker-entrypoint.sh    
	Setup email and password in \mysite\\mysite\settings.py (GMAIL req. 2 step password from June 2022)
	cd mysite\
	Open Doker Desktop in Windows	
	docker-compose up
	http://127.0.0.1:8000/
	Test:
	docker-compose run web python3 manage.py test

Testing:
--------

	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report (or) coverage html

Installation (not checked):
-------------

	Create new folder "SearchEngineREST" and open it:
	git clone https://github.com/marcin86junior/SearchEngineREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd mysite\
	python manage.py migrate
	python manage.py makemigrations
	python .\manage.py runserver
	http://127.0.0.1:8000/

Issues
------

	At the moment there are few issuse:
	- There is bug that happens every 1/1000 - XLM package have no author (xc_author) - hard to catch - now it's " "
	- Redis have diffrent time (-2h)