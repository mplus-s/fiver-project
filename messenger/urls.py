from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StartMessaging
# from products.views import TransactionViewSet

urlpatterns = [
    path('<str:product_id>', StartMessaging.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)