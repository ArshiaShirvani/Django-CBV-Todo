from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.

class UserCreateView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = "/login/"

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "login.html"
    fields = "username","password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("signup")