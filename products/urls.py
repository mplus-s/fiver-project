from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CartItemViewSet, ProductList, ProductDetail
from rest_framework.routers import DefaultRouter, SimpleRouter

cart_item_router = SimpleRouter()
cart_item_router.register('cartitems', CartItemViewSet, basename='cartitems')
urlpatterns = [
    # path('', ProductList.as_view()),
    path('', ProductList.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProductDetail.as_view()),
    path('cart/', include(cart_item_router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)