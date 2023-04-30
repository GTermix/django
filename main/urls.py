from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('order/', add_order, name='order'),
    path('furniture/', index, name='about'),
]
