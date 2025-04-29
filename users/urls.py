from django.urls import path
from .views import UserProfileView
from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
