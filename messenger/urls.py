from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StartMessaging, Conversation

urlpatterns = [
    path('', StartMessaging.as_view()),
    path('<str:product_uid>', Conversation.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)