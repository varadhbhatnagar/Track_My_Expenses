from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserLoginForm, UserSignupForm, ProfileForm
from .models import *


def home(request):
    """!
    @brief Landing page
    """
    return render(request, 'Sl_proj/home.html', {})


class UserSignupFormView(View):
    """!
    @detailed SignUp for User
    """
    user_form_class = UserSignupForm
    profile_form_class = ProfileForm
    template_name = 'registration/registration_form.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        profile_form = self.profile_form_class(None)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        profile_form = self.profile_form_class(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            Profile.objects.create(
                user=user,
                First_Name=profile_form.cleaned_data['First_Name'],
                Last_Name=profile_form.cleaned_data['Last_Name'],
                Mobile_Number=profile_form.cleaned_data['Mobile_Number'],
                Annual_Income =profile_form.cleaned_data['Annual_Income']
            )

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class UserLoginFormView(View):
    """!
    @detailed Login for User
    """
    user_form_class = UserLoginForm
    template_name = 'registration/login_form.html'

    def get(self, request):
        user_form = self.user_form_class(None)
        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request):
        user_form = self.user_form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')

        return render(request, self.template_name, {'user_form': user_form})


def user_logout(request):
    """!
    @detailed end the sessions for a User
    @return path to home page
    """
    logout(request)
    return redirect('home')


def profile(request):
    """!
    @detailed User profile description
    @return path to profile page along with profile information
    """
    my_profile = request.user.profile
    context = {'my_profile': my_profile}
    return render(request, 'Sl_proj/profile.html', context)


