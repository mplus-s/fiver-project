from rest_framework import serializers
from .models import Product
from categories.models import Category
from users.models import User
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=False, queryset=Category.objects.all(), slug_field="name")
    added_by = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        exclude = ("id", "added_at",)
