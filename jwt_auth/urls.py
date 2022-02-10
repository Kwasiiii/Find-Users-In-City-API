from xml.etree.ElementInclude import include
from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', UserDetailView.as_view()),
    path('users/',UserListView.as_view()) 
]