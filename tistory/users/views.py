from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, Loginform
from .models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/user/login/'

    def form_valid(self, form):
        user = User(
            username=form.data.get('username'),
            email=form.data.get('email'),
            gender=form.data.get('gender'),
            password=make_password(form.data.get('password')),
            user_level = 'normal_user',
        )
        user.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = Loginform
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)
    
def Logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')
