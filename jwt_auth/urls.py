from xml.etree.ElementInclude import include
from django.urls import path
from .views import CityUsersView, RegisterView, LoginView, UserDetailView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', UserDetailView.as_view()),
    path('users/',UserListView.as_view()),
    path('city/<str:city>/users/', CityUsersView.as_view()) 
]