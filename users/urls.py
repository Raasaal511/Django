from . import views
from django.urls import path


urlpatterns = [
    path(r'login/', views.UserLoginView.as_view(), name='user_login'),
    path(r'register/', views.RegisterView.as_view(), name='register'),
    path(r'logout/', views.UserLogoutView.as_view(), name='logout'),
    path(r'profile/', views.user_profile_view, name='profile')
]