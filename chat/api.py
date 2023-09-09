from rest_framework import viewsets, views
from django.http import JsonResponse, HttpRequest
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist

class Register(views.APIView):

    def get(self, request):
        return JsonResponse({
            "username": "Arafat"
        })
    
    def post(self, request: HttpRequest):
        """
        Create a new user
        """
        fields = ["first_name", "last_name", "email", "username", "password", "c_password"]
        for f in fields:
            if f not in request.POST:
                raise FieldDoesNotExist(f"{f} is missing.")
            
        return JsonResponse({
            "status": "Registered"
        })