from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# 
# 
from .forms import UserForm, UserClientForm, UserSupplierForm


class SignUp(View):
    @method_decorator(login_required(login_url='login:login'))
    def get(self, request):
        user_form = UserForm()

        return render(request, 'acl_sign_template.html', {
            'form': user_form
        })
    
    @method_decorator(login_required(login_url='login:login'))
    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

            return redirect('home:home')


class SignClient(View):
    @method_decorator(login_required(login_url='login:login'))
    def get(self, request):
        client_form = UserClientForm()

        return render(request, 'acl_sign_template.html', {
            'form': client_form
        })

    @method_decorator(login_required(login_url='login:login'))
    def post(self, request):
        client_form = UserClientForm(request.POST)

        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.save()

            return redirect('home:home')


class SignSupplier(View):
    @method_decorator(login_required(login_url='login:login'))
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