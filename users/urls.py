from django.contrib import admin
from django.urls import path, include
from .views import register, profile
#from .views import UserProfileListView
urlpatterns = [
    path('register/', register, name="users-register"),
    #path('profile/', UserProfileListView.as_view(), name="profile" )
    path('profile/', profile, name='profile'),
    
]