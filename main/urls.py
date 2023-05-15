from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                      template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
                  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
                      template_name='password/password_reset_complete.html'), name='password_reset_complete'),
                  path("password_reset", password_reset_request.as_view(), name="password_reset"),

                  path('register/', reg_form, name='rgf'),
                  path('logout', logout_, name='logout'),
                  path('login', login_, name='login'),
                  path('products/<slug:cat_slug>/', Products.as_view(), name='cat_detail'),
                  path('', index, name='index'),
                  path('customer/', customer_page, name='customer'),
                  path('contact/', contact_add, name='contact'),
                  path('productsadd/', product_add, name='product'),
                  path("products/", Products.as_view(), name="prdc"),
                  path('order/', add_order, name='order'),
                  path('product/<int:pk>/', product_details, name='prdct'),
                  path('address/', address_page, name='address'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
