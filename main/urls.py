from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='index'),
    path('furniture/', furniture_page, name='furniture'),
    path('shop/', shop_page, name='shop'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('signup/', registration, name='reg'),
]
