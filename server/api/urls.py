from django.conf.urls import url, include
from rest_framework import routers
from ..api import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^auth/login/", views.LoginView.as_view(), name="auth_register"),
    url(r"^auth/logout/", views.LogoutView.as_view(), name="auth_register"),
    url(r"^auth/register/", views.RegisterView.as_view(), name="auth_register"),
    url(r"^auth-api/", include("rest_framework.urls", namespace="rest_framework")),
]
