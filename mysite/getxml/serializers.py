from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Package

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        #read_only_fields = ('author', 'title', 'link', 'guid', 'description', 'pubDate',)
        permission_classes = [IsAuthenticatedOrReadOnly]
