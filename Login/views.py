from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth import login, logout
from acl.models import User as UserModel


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
                return redirect('home:home')
            
            return render(request, 'login.html', {'Error': 'Senha Incorreta!'})
        
        except user.DoesNotExist as e:
            return render(request, 'login.html', {'Error': 'Credenciais Incorretas! Usuário não existente'})