from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('', CategoryList.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', CategoryDetail.as_view({'patch': 'partial_update',
                                    'delete': 'destroy',
                                    'get': 'retrieve'
                                    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)