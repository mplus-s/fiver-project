from .views import UserActivationView
from django.conf.urls import url , include
from django.urls import path
from products.views import CartItemViewSet
from rest_framework.routers import  SimpleRouter

cart_item_router = SimpleRouter()
cart_item_router.register('cartitems', CartItemViewSet, basename='cartitems')

urlpatterns = [
    url(r'^users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', UserActivationView.as_view()),
    path('cart/', include(cart_item_router.urls)),

]