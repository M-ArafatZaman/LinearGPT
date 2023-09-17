from django.urls import path
from .api import ChatView

appname = "api"
urlpatterns = [
    path("chatview/", ChatView.as_view(), name="register")
]