from django.conf import settings
from django.core.mail import EmailMessage
from django.core import serializers

from celery import shared_task
from celery.utils.log import get_task_logger

import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample test - task just ran every minute.")

@shared_task
def collect_data_task():
    from getxml.models import Package

    logger.info("Data collected.")
    url = 'https://www.googleapis.com/books/v1/volumes?q=war'
    data1 = requests.get(url).json()
    with urlopen('https://pypi.org/rss/packages.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        xc = 4
        while xc < len(root[0]):
            for child in root[0][xc]:
                if child.tag == 'author':
                    xc_author = child.text
                if child.tag == 'title':
                    xc_title = child.text
                if child.tag == 'pubDate':
                    xc_pubDate = child.text
                if child.tag == 'link':
                    xc_link = child.text
                if child.tag == 'guid':
                    xc_guid = child.text
                if child.tag == 'description':
                    xc_description = child.text
            Package.objects.create(
                author = xc_author,
                title = xc_title,           
                pubDate = xc_pubDate,
                link = xc_link,
                guid = xc_guid,
                description = xc_description,
            )
            xc = xc + 1 

@shared_task
def backup_task():
    from getxml.models import Package

    logger.info("Creating email with backup..")
    subject = "Backup email from SearchEngineREST"
    from_email = settings.EMAIL_HOST_USER
    data = serializers.serialize("json", Package.objects.all())
    
    out = open("data.json", "w")
    out.write(data)
    out.close()

    if data == '[]':
        message = (
            f"Dear client!\n\nThis email is generated automatically. Your app is still is running! There is no data in database.\n\nBest regards\nSearchEngineREST team") #+datax
    else:
        message = (
        f"Dear client!\n\nThis email is generated automatically. Your app is still is running! I'm attaching to letter data.json with backup database.\n\nBest regards\nSearchEngineREST team") #+datax
    
    to = settings.EMAIL_HOST_USER # "abc@gmail.com" or standard from settings.py
    email = EmailMessage(
        subject,
        message,
        from_email,
        to=[to]
    )
    if data == '[]':
        pass
    else:
        email.attach_file('data.json')
    email.send()
    logger.info("Finishing email...")
