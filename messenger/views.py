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
from django.shortcuts import get_object_or_404
class MultipleFieldLookupORMixin(object):
    """
    Actual code http://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            try:                                  # Get the result with one or more fields.
                filter[field] = self.kwargs[field]
            except Exception:
                pass
        return get_object_or_404(queryset, **filter)  # Lookup the object
class StartMessaging(MultipleFieldLookupORMixin,viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ('product_id','buyer_id')

    def get_queryset(self):
        user = self.request.user
        productt = Product.objects.get(id = self.kwargs["product_id"])
        owner = productt.added_by
        if user.id == owner.id:
            queryset = Message.objects.filter( Q (seller=owner.id) & Q(buyer=self.kwargs["buyer_id"]) & Q (product_id =self.kwargs["product_id"]))
            return queryset            
        else:
            queryset = Message.objects.filter( Q (seller=owner.id ) & Q(buyer=user.id) & Q (product_id =self.kwargs["product_id"]))
            return queryset
