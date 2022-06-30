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

Installation:
-------------


	Create new folder "SearchEngineREST" and open it:
	git clone https://github.com/marcin86junior/PackageSearchEngineREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd mysite\
	python manage.py migrate
	python manage.py makemigrations
	python .\manage.py runserver
	http://127.0.0.1:8000/


Testing:
--------

	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report (or) coverage html


Docker:
-------

	Create new folder "SearchEngineREST" and open it:
	git clone https://github.com/marcin86junior/PackageSearchEngineREST.git .
	cd mysite\
	"Open Doker Desktop"
	"CRLF->LF" in \django_rest_imageupload_backend\docker-entrypoint.sh    
	docker-compose up
	http://127.0.0.1:8000/
	Test:
	docker-compose run web python3 manage.py test


Fixtures
--------


	Data included in fixtures:

	User / Password / Assigned group / Added pictures to model
	b1 / 123 / Basic / 2
	p2 / 123 / Premium / 2
	e3 / 123 / Enterprice/ 2 
	c4 / 123 / Custom/ 2


Issues
------


	At the moment there are few issuse:

	- ................