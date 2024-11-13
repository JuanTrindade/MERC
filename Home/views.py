from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# 
# 
# class HomeBase(LoginRequiredMixin):
#     login_url = 'login'


class Home(View):
    @method_decorator(login_required(login_url='login:login'))
    def get(self, request):
        return render(request, 'home.html')

class ListEmployee(ListView):
    template_name = 'base.html'