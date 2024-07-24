from django.contrib.auth.views import LogoutView
from django.urls import path

import auth.views as views
from .views import LoginView, RegistrationView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
