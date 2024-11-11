from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout, authenticate
from acl.models import User as UserModel
# 
# 
from .forms import UserForm

class Login(View):
    def get(self, request):
        logout(request)
        return render(request, 'login.html')
    
    def post(self, request):
        request_email = request.POST.get('email')
        request_password = request.POST.get('password')
        user = UserModel
        
        try:
            user_obj = user.objects.get(email=request_email)
            is_password_correct = user_obj.check_password(request_password)
            
            if is_password_correct:     
                login(request, user_obj)
                return redirect('home')
            
            return render(request, 'login.html', {'Error': 'Senha Incorreta!'})
        
        except user.DoesNotExist as e:
            return render(request, 'login.html', {'Error': 'Credenciais Incorretas! Usuário não existente'})


class SignUp(View):
    def get(self, request):
        user_form = UserForm()

        return render(request, 'signup.html', {
            'form': user_form
        })
    
    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user.password)
            user.save()

            return redirect('login')
    
# def render_login(request):
#     return render(request, 'login.html')