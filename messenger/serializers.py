from rest_framework import serializers
from .models import Message
from products.models import Product
from users.models import User
from djoser.utils import settings
from rest_framework import serializers
from datetime import datetime
import json
from rest_framework.exceptions import NotAcceptable


class InitializeMessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Product.objects.all(), default=serializers.CurrentUserDefault())
    product = serializers.SlugRelatedField(
        read_only=False, queryset=Product.objects.all(), slug_field="uid")
    messages = serializers.CharField()

    class Meta:
        model = Message
        exclude = ('parties', 'id')

    def save(self, **kwargs):

        sender = self.validated_data["sender"]
        product = self.validated_data["product"]
        
        kwargs["parties"] = [sender.id, product.added_by.id]

        # if parties conversation about product exists, simly update messages
        messages = [json.dumps({
            "sender": sender.id,
            "message": self.validated_data["messages"],
            "sent_at": f"{datetime.now()}"
        }), ]
        
        del self.validated_data["sender"]
        
        self.validated_data["messages"] = messages

        message = Message.objects.filter(product=product, parties=kwargs["parties"]).first()

        if message:
            message.messages.append(self.validated_data['messages'][0])
            message.save()
            return message
        return super().save(**kwargs)



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude  = ("id", "parties",)
    
    