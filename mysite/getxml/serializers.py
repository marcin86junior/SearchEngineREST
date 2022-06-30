from rest_framework import serializers
from .models import Packeage

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Packeage
        fields = '__all__'
        read_only_fields = ('author', 'title', 'link', 'guid', 'description', 'pubDate',)
