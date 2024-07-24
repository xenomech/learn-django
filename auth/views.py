from django.urls import reverse_lazy
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.shortcuts import redirect


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("todo:list_all_todo")

    def form_valid(self, form):
        user = form.save()
        print(user)
        login(self.request, user)
        return redirect(self.success_url)


class LoginView(LoginView):
    authentication_form = LoginForm
    success_url = reverse_lazy("todo:list_all_todo")
    template_name = "auth/login.html"
