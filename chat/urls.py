from django.urls import path
from .api import Register

appname = "api"
urlpatterns = [
    path("register", Register.as_view(), name="register")
]