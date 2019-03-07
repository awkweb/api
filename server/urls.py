from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^v1/", include("server.api.urls")),
    path("a/", admin.site.urls),
    url("h/", views.health_check, name="health_check"),
    url("", views.index, name="index"),
]
