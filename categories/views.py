from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from avina.utils import PermissionMixin


class CategoryList(PermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {'create': [IsAdminUser],
                                    'list': [IsAuthenticated]}



class CategoryDetail(PermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {'partial_update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'retrieve': [IsAuthenticated]
                                    }
