from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', index, name='index'),
                  path('customer/', customer_page, name='customer'),
                  path('contact/', contact_add, name='contact'),
                  path('productsadd/', product_add, name='product'),
                  path("products/", products, name="prdc"),
                  path('order/', add_order, name='order'),
                  path('product/<int:pk>/', product_details, name='prdct'),
                  path('address/', address_page, name='address'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
