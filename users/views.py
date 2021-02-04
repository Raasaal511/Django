from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .models import UserProfile
from .forms import UserLoginForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import CreateView
from django.contrib.auth.models import User


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = '/'


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        form_valid = super().form_valid(form)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)

        return form_valid


class UserLogoutView(LogoutView):
    next_page = '/'


def user_profile_view(request):
    user_views = UserProfile()

    context = {'user_views': user_views}

    return render(request, 'profile.html', context)