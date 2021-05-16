from rest_framework import serializers
from .models import Product
from categories.models import Category
from users.models import User
from rest_framework import serializers
from drf_base64.fields import Base64ImageField

class ProductSerializer(serializers.ModelSerializer):
    photo1 = Base64ImageField()
    photo2 = Base64ImageField()
    photo3 = Base64ImageField()
    photo4 = Base64ImageField()

    category = serializers.SlugRelatedField(read_only=False, queryset=Category.objects.all(), slug_field="name")
    added_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        exclude = ("id", "added_at",)
