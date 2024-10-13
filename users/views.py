from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:register")

    def form_valid(self, form) -> HttpResponse:
        print(form, type(form))
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "users/profile.html"
