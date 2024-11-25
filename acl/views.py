from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, FormView
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
# 
# 
from .forms import UserForm, UserClientForm, UserSupplierForm

class RegisterBase(LoginRequiredMixin, FormView):
    login_url = 'login:login'


class SignUp(RegisterBase):
    template_name = 'acl_sign_template.html'
    form_class = UserForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.save()

        return super().form_valid(user)


class RegisterClient(RegisterBase):
    template_name = 'acl_sign_template.html'
    form_class = UserClientForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        client = form.save(commit=False)
        client.save()

        return super().form_valid(client)


class RegisterSupplier(RegisterBase):
    template_name = 'acl_sign_template.html'
    form_class = UserSupplierForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        supplier = form.save(commit=False)
        supplier.save()

        return super().form_valid(supplier)