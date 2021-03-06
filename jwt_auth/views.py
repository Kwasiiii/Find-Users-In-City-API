from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import jwt

from jwt_auth.serializer.populated import PopulatedProductSerializer
from .serializer.common import UserSerializer

from city.models import City
from city.serializers.common import CitySerializer

User = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({'message': 'Registration Successful'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginView(APIView):
    
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user_to_login = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied(detail="Invalid Credentials")
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail="Invalid Credentials")
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(dt.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm= 'HS256'
        )
        return Response({'token':token, 'message': f"Welcome back, {user_to_login.username}", 'username':{user_to_login.username}, 'email':{user_to_login.email}, 'first_name':{user_to_login.first_name}, 'last_name': {user_to_login.last_name}})

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)

class UserListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request):
        user = User.objects.all()
        serialized_user = PopulatedProductSerializer(user, many = True)
        return Response(serialized_user.data, status=status.HTTP_200_OK)

class CityUsersView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, _request, city):
        user = User.objects.filter(city__name = city)
        cities = City.objects.get(name = city)
        serialized_city = CitySerializer(cities)
        print(serialized_city)
        serialized_user = PopulatedProductSerializer(user, many = True)
        return Response([serialized_user.data, serialized_city.data], status= status.HTTP_200_OK)