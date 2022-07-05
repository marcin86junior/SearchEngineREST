SearchEngineREST
================

![alt text](http://marcin86.pythonanywhere.com/static/SearchEngineREST.JPG)

Overview
--------

SearchEngineREST is a web application for searching latest python package. 
Django/REST technology is used for searching / database and recovery.
On "options" site you can: add data, create rocovery file, delete data.

Celery and Celery-beat have now 3 tasks:

	- collecting data at 8:00 (8 AM)
	- send recovery email with attachment data.json at 23:00 (11 PM) or send information if database is empty
	- run test_task every minute

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
	Please setup email and password in \mysite\mysite\settings.py (GMAIL req. 2 step password from June 2022)
	Please setup pagination in \mysite\mysite\settings.py -> 'PAGE_SIZE': 10,
	Please setup crontab in \mysite\mysite\settings.py -> now it's 8:00 / 23:00 (you can change to every minute)
	Run Doker Desktop in Windows.	
	cd mysite\
	docker-compose up
	http://127.0.0.1:8000/

	Docker tests:
	You can add to \mysite\docker-entrypoint.sh this code:
	echo "Test website"
	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report
	
	docker-compose up
	In terminal you will see coverage.

Testing:
--------

	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report (or) coverage html

Installation (working without celery-beat):
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

	# probably we can run in new terminal celery / celery-beat somehow
	..........

	python manage.py test 

Issues
------

	- (FIXED) There is bug that happens every 1/300. Bug hard to catch. XLM package have no author (xc_author). Now it's fixed to author="".
	- (FIXED) Redis have diffrent time (-2h). Hours in settings are now -2h so it's correct.
	- (FIXED) Wrong command in readme for tests in Docker: "docker-compose run web python3 manage.py test". Added test to docker-entrypoint.sh.
