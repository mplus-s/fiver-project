from rest_framework import serializers
from .models import Category
from drf_base64.fields import Base64ImageField
class CategorySerializer(serializers.ModelSerializer):
    photo = Base64ImageField()
    class Meta:
        model = Category
        fields = ("id", "name", "photo",)
        # exclude = ("id",)