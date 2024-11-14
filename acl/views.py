from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
# 
# 
from .forms import UserForm, UserClientForm, UserSupplierForm

class RegisterBase(LoginRequiredMixin, View):
    login_url = 'login:login'


class SignUp(RegisterBase):
    def get(self, request):
        user_form = UserForm()

        return render(request, 'acl_sign_template.html', {
            'form': user_form
        })
    
    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

            return redirect('home:home')


class SignClient(RegisterBase):
    def get(self, request):
        client_form = UserClientForm()

        return render(request, 'acl_sign_template.html', {
            'form': client_form
        })

    def post(self, request):
        client_form = UserClientForm(request.POST)

        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.save()

            return redirect('home:home')


class SignSupplier(RegisterBase):
    def get(self, request):
        supplier_form = UserSupplierForm()
        # breakpoint()

        return render(request, 'acl_sign_template.html', {
            'form': supplier_form
        })

    def post(self, request):
        supplier_form = UserSupplierForm(request.POST)

        if supplier_form.is_valid():
            supplier = supplier_form.save(commit=False)
            supplier.save()

            return redirect('home:home')