from rest_framework import viewsets, views
from django.http import JsonResponse

class Register(views.APIView):

    def get(self, request):
        return JsonResponse({
            "username": "Arafat"
        })