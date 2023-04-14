from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('about/', about_page),
    path('contact/', contact_page)
]
