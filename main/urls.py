from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
                  path('', CategoryListCreateAPIView.as_view()),
                  path('cat/<int:pk>/', CategoryDetailUpdateDelete.as_view()),
                  path('api/v1/auth/', include('dj_rest_auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
