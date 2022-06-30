from rest_framework import viewsets, generics
from getxml.serializers import BookSerializer
from .models import Packeage

from rest_framework import filters
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from django.shortcuts import render, redirect, render
import requests
import xml.etree.ElementTree as ET

from urllib.parse import urlparse
from urllib.request import urlopen

from django.http import JsonResponse
import json


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = Packeage.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = {'author': ['startswith'], 'title': ['startswith'] ,'pubDate': ['startswith'] }
    search_fields = ['author', 'title',]
    ordering_fields = ['published_date','id']

class BookYearList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the year.
        """
        year = self.kwargs['year']
        return Packeage.objects.filter(published_date = year)

class BookAuthorList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name.
        """
        authorname = self.kwargs['authorname']
        return Packeage.objects.filter(author = authorname)

class BookAuthorList2(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name 1 or author name 2.
        """
        authorname1 = self.kwargs['authorname1']
        authorname2 = self.kwargs['authorname2']
        print(authorname1)
        print(authorname2)
        return Packeage.objects.filter(author = authorname1).filter(author = authorname2)

class BookTitleList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name.
        """
        titlename = self.kwargs['titlename']
        return Packeage.objects.filter(title = titlename)

def options(request):
    return render(request, 'booksapi/options.html')

def main(request):
    return render(request, 'booksapi/main.html')

def getdata1(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    
    # Read the JSON
    data1 = requests.get(url).json()

    # Create a Django model object for each object in the JSON 
    for book_data in data1['items']:
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']

        book = Packeage.objects.create(
            title=title,
            author=authors, 
            pubDate=published_date, 
           )

    return render(request, 'booksapi/data1added.html')

def getdata2(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=war'

    # Read the JSON
    data1 = requests.get(url).json()

    # Create a Django model object for each object in the JSON 
    for book_data in data1['items']:
        volume_info = book_data['volumeInfo']
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']
     
        book = Packeage.objects.create(
            title=title,
            author=authors, 
            pubDate=published_date, 
           )
           
    return render(request, 'booksapi/data2added.html')

def getdata3(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=war'
    data1 = requests.get(url).json()

    
    with urlopen('https://pypi.org/rss/packages.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        #print(len(root[0].tag)

        #for child in root[0]:
        #    print(child.tag, child.attrib)

        #print(len(root[0]))
        #print('----------------------------')
        xc = 4
        while xc < len(root[0]):
            for child in root[0][xc]:
                #print('CT:',child.tag,'CT:',child.text,)
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

            book = Packeage.objects.create(
                author = 'xc_author,',
                title = xc_title,           
                pubDate = xc_pubDate,
                link = xc_link,
                guid = xc_guid,
                description = xc_description,
                #categories=categoriesx,
                #average_rating=ratingsCountx,
                #ratings_count = ratingsCountx,
            )
            xc = xc + 1 
    # Read the JSON


    '''
    # Create a Django model object for each object in the JSON 
    for book_data in data1['items']:
        volume_info = book_data['volumeInfo']
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']
        categoriesx = volume_info.get("categories", None)
        averageRatingx = volume_info.get("averageRating", None)
        ratingsCountx = volume_info.get("ratingsCount", None)
        thumbnailx = volume_info.get("imageLinks", None)
        thumbnaily = thumbnailx.get("thumbnail", None)
     
        book = books.objects.create(
            title=title,authors=authors, 
            published_date=published_date, 
            categories=categoriesx,
            average_rating=ratingsCountx,
            ratings_count = ratingsCountx,
            thumbnail=thumbnaily,
           )
    '''
           
    return render(request, 'booksapi/data2added.html')

def deletedata2(request):
    for booksx in Packeage.objects.all():
        #if booksx.id > 11:
            booksx.delete()
    return render(request, 'booksapi/data2deleted.html')

def json(request):
    data = list(Packeage.objects.values())
    return JsonResponse(data, safe=False)