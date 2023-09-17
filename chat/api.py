from rest_framework import viewsets, views
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ChatView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request: HttpRequest):
        return JsonResponse({
            "username": request.user.username
        })