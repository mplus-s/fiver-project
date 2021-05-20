import re
from messenger.models import Message
from rest_framework import serializers
from .models import Product , CartItem
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
        exclude = ( "added_at",)

class CartitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

    def validate(self, validated_data):
        if validated_data["seller_confirmation"] == True & validated_data["buyer_confirmation"] == True:
            validated_data["status"] = "Sold"
            return validated_data
        return validated_data