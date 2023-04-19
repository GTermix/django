from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page),
    path('about/', about_page, name="about"),
    path('contact/', contact_page, name="contact"),
    path('registration/', registration_page, name="registration")
]
