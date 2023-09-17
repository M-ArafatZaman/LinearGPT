from rest_framework.views import APIView
from django.http import JsonResponse, HttpRequest
from django.core.exceptions import FieldDoesNotExist, ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Q
from knox.models import AuthToken
from rest_framework.permissions import AllowAny

class Register(APIView):

    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest):
        """
        Create a new user
        """
        # Validate all the fields
        fields = ["first_name", "last_name", "email", "username", "password", "c_password"]
        for f in fields:
            if f not in request.POST:
                raise FieldDoesNotExist(f"{f} is missing.")

        # Get all the required data
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]

        # Ensure that passwords are the same
        if password != c_password:
            raise ValidationError("Passwords do not match.")

        # Create account
        new_user = User(
            first_name=first_name, last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        # Set password
        new_user.set_password(password)

        # Save
        new_user.save()

        # Generate Auth Token
        _, token = AuthToken.objects.create(new_user)

        # Return the token
        return JsonResponse({
            "status": 200,
            "token": token
        })
    

# Login class
class Login(APIView):

    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest) -> JsonResponse:
        """
        Create a new token and return it
        """
        # Validate fields
        if "username" not in request.POST and "email" not in request.POST:
            # Either username or email is required to login
            return JsonResponse({
                "status": 401,
                "message": "username or email is missing."
            }, status=401)
        if "password" not in request.POST:
            return JsonResponse({
                "status": 401,
                "message": "password is missing."
            }, status=401)
        
        # Get data
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST["password"]

        try: 
            user = User.objects.get(Q(username=username) | Q(email=email))

        except ObjectDoesNotExist:
            # No user found
            return JsonResponse({
                "status": 401,
                "messaeg": "Invalid credentials."
            }, status=401)
        
        if user.check_password(password):
            # Create and return a new token
            _, token = AuthToken.objects.create(user)

            return JsonResponse({
                "status": 200,
                "token": token
            })
            
        else:
            # Wrong password
            return JsonResponse({
                "status": 401,
                "messaeg": "Invalid credentials."
            }, status=401)