from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# 
# 
from .models import Product as ProductModel
from .forms import ProductForm, StockForm

class ProductBase(LoginRequiredMixin):
    login_url = 'login:login'


class ProductCreate(FormView):
    title = 'CADASTRO DE PRODUTOS'
    template_name = 'register_product.html'
    fields = '__all__'
    form_class = ProductForm #Django ja faz o trabalho de chamar a classe form mesmo sem os parênteses

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['form_stock'] = StockForm

        return context

    def post(self, request):
        context = self.get_context_data()
        
        product_form = context['form']
        stock_form = context['form_stock'](self.request.POST)
        
        self.validating_form(product_form, stock_form)

        return redirect('home:home')
        

    def validating_form(self, product_form, stock_form):
        if product_form.is_valid():
            product_object = product_form.save(commit=False)
            product_object.save()
        
            if stock_form.is_valid():
                stock_object = stock_form.save(commit=False)
                stock_object.product = product_object

                stock_object.save()