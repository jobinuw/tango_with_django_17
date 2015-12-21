from rest_framework import serializers
from rango.models import Category,Page


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'views', 'likes', 'slug')