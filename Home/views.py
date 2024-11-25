from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# 
# 
class HomeBase(LoginRequiredMixin, View):
    login_url = 'login:login'
    redirect_field_name = 'redirect'

class Home(HomeBase):
    def get(self, request):
        return render(request, 'home.html')
