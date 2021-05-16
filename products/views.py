from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]


    def perform_destroy(self, instance):
        if self.request.user == instance.added_by:
            return super().perform_destroy(instance)
        raise PermissionDenied()

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.added_by:
            return super().perform_update(serializer)
        raise PermissionDenied()
        