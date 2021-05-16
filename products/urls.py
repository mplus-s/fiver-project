from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductList, ProductDetail

urlpatterns = [
    # path('', ProductList.as_view()),
    path('', ProductList.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)