from django.urls import path, include
from .views import RegisterView, LoginView, Logout

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', Logout),
]