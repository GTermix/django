from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"cat",CatsViewSet,basename="cat")
urlpatterns = router.urls


# urlpatterns = [
#                   path('', CategoryClass.as_view({"get": "list"})),
#                   path('cat/<int:pk>/', CategoryClass.as_view(
#                       {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})),
#                   # path('', CategoryListCreateAPIView.as_view()),
#                   # path('cat/<int:pk>/', CategoryDetailUpdateDelete.as_view()),
#                   path('api/v1/auth/', include('dj_rest_auth.urls')),
#                   path('api/v1/auth/registration/', RegisterUser.as_view())
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
