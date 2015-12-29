from rest_framework import serializers
from rango.models import Category,Page


class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'views', 'likes', 'slug')