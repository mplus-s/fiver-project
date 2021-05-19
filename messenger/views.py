from products.models import Product
from django.db.models.base import Model
from rest_framework import generics 
from .models import Message
from products.models import Product
from .serializers import  MessageSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets
from django.db.models import Q

class StartMessaging(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "product_id"

    def get_queryset(self):
        user = self.request.user
        productt = Product.objects.get(id = self.kwargs["product_id"])
        owner = productt.added_by
        queryset = Message.objects.filter( Q (seller=owner.id ) & Q(buyer=user.id) & Q (product_id =self.kwargs["product_id"]))
        return queryset



