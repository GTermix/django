from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('customer/', customer_page, name='customer'),
    path('contact/', contact_add, name='contact'),
    path('products/', product_add, name='product'),
    path('order/', add_order, name='order'),
    path('address/', address_page, name='address'),
]
