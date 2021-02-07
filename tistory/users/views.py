from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm
from .models import User

# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = User(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            user_level = 'user',
        )
        user.save()
        return super().form_valid(form)