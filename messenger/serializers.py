from rest_framework import serializers
from .models import Message
from products.models import Product
from users.models import User
from djoser.utils import settings
from rest_framework import serializers
from datetime import datetime
import json
from rest_framework.exceptions import NotAcceptable


class MessageSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(many=False, slug_field='id', queryset=User.objects.all(),default=serializers.CurrentUserDefault())
    buyer = serializers.SlugRelatedField(many=False, slug_field='id', queryset=User.objects.all(),)

    product = serializers.SlugRelatedField(
        read_only=False, queryset=Product.objects.all(), slug_field="id")

    class Meta:
        model = Message
        exclude = ('id',)
