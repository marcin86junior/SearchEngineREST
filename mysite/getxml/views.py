from rest_framework import viewsets, generics
from getxml.serializers import BookSerializer
from .models import Package

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
from .forms import ReadFileForm

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = Package.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = {'author': ['startswith'], 'title': ['startswith'] ,'pubDate': ['startswith'] }
    search_fields = ['author', 'title', 'description',]
    ordering_fields = ['published_date','id']

class BookYearList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the year.
        """
        year = self.kwargs['year']
        return Package.objects.filter(published_date = year)

class BookAuthorList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name.
        """
        authorname = self.kwargs['authorname']
        return Package.objects.filter(author = authorname)

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
        return Package.objects.filter(author = authorname1).filter(author = authorname2)

class BookTitleList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name.
        """
        titlename = self.kwargs['titlename']
        return Package.objects.filter(title = titlename)

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
        volume_info = book_data['volumeInfo']
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']

        book = Package.objects.create(
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
     
        book = Package.objects.create(
            title=title,
            author=authors, 
            pubDate=published_date, 
           )
           
    return render(request, 'booksapi/data2added.html')

def getdata3(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=war'

    # Read the JSON
    data1 = requests.get(url).json()

    # Create a Django model object for each object in the XML 
    with urlopen('https://pypi.org/rss/packages.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()
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
            book = Package.objects.create(
                author = xc_author,
                title = xc_title,           
                pubDate = xc_pubDate,
                link = xc_link,
                guid = xc_guid,
                description = xc_description,
            )
            xc = xc + 1        
    return render(request, 'booksapi/data2added.html')

def deletedata(request):
    for booksx in Package.objects.all():
            booksx.delete()
    return render(request, 'booksapi/data2deleted.html')

def json(request):
    data = list(Package.objects.values())
    return JsonResponse(data, safe=False)

def read_file(request):
    form = ReadFileForm()
    if request.method == 'POST':
        form = ReadFileForm(request.POST, request.FILES)
        if form.is_valid():
            import json
            content = request.FILES['file'].read()

            # Read the JSON
            data  = json.loads(content)

            # Create a Django model object for each object in the JSON 
            i=0
            while i < len(data):
                title_xc = (data[i]['title'])
                author_xc = (data[i]['author'])
                pubDate_xc = (data[i]['pubDate'])
                link_xc = (data[i]['link'])
                description_xc = (data[i]['description'])
                guid_xc = (data[i]['guid'])
            
                book = Package.objects.create(
                    title = title_xc,
                    author = author_xc,
                    pubDate = pubDate_xc,
                    link = link_xc,
                    guid = guid_xc,
                    description = description_xc
                )
                i = i + 1
            return render(request, 'booksapi/data2added.html')
    return render(request, 'booksapi/upload.html', locals())