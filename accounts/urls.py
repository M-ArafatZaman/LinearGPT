from django.urls import path 
from .api import Register

appname="accounts-api"
urlpatterns = [
    path("register/", view=Register.as_view())
]
