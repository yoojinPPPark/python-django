from django.urls import path
from .views import index, test2, test3

urlpatterns = [
    path('', index, name='index'),
    path('test2/', test2, name='test2'),
    path('test3/', test3, name='test3'),
]
