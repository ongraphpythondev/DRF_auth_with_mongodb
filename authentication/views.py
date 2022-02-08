from venv import create
from rest_framework.views import APIView
from .serializers import RegistrationSerializer 
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from rest_framework.authtoken.models import Token




# Create your views here.
def generate_token(email):
    user = CustomUser.objects.filter(email = email).first()
    token ,created= Token.objects.get_or_create(user=user)
    return token


class Registration(APIView):

    def post(self , request):
        serializer = RegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        token = generate_token(serializer.data["email"])

        return Response({"user data":serializer.data , "token":str(token) , "status":f"Account created"}, status=status.HTTP_201_CREATED)



class Login(APIView):

    def post(self , request):
        # user = authenticate(email = request.data["email"], password = request.data["password"])
        user = CustomUser.objects.filter(email = request.data["email"]).first()
        if user is None:
            return Response( {"status":f"User not found"}, status = status.HTTP_404_NOT_FOUND)

        if user.password != request.data["password"]:
            return Response( {"status":f"Password is incorrect"}, status = status.HTTP_404_NOT_FOUND)

            
        token = generate_token(request.data["email"])

        return Response({"token":str(token) , "status":f"Account created"}, status=status.HTTP_200_OK)
