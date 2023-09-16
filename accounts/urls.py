from django.urls import path 
from .api import Register, Login

appname="accounts-api"
urlpatterns = [
    path("register/", view=Register.as_view()),
    path("login/", view=Login.as_view())
]
