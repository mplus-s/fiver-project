from .views import UserActivationView
from django.conf.urls import url


urlpatterns = [
    url(r'^users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', UserActivationView.as_view()),
]