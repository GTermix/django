from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('cats/detail/', CatDetailCreateView.as_view(), name='cr_cat'),
    path('cat/<int:pk>/', CatDeleteEditView.as_view(), name='sdfsd'),
]
