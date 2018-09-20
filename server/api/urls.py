from django.conf.urls import url, include
from rest_framework import routers
from server.api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth-api/', include('rest_framework.urls', namespace='rest_framework')),
]
