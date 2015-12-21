from rest_framework import serializers
from rango.models import Category,Page, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'views', 'likes', 'slug')