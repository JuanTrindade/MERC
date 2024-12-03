from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, ListView, DeleteView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
# 
# 
from .models import (
    Product as ProductModel, 
    StockHistory as StockModel, 
    ProductSummary as SummaryModel
)
from .forms import ProductForm, StockForm


class ProductBase(LoginRequiredMixin):
    login_url = 'login:login'
    redirect_field_name = 'redirect'


class ProductList(ProductBase, ListView):
    template_name = 'CRUDE_Product/list_product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # breakpoint()
        return context
    

class ProductCreate(ProductBase, FormView):
    title = 'CADASTRO DE PRODUTOS'
    template_name = 'CRUDE_Product/register_product.html'
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

        if product_form.is_valid():
            product_object = product_form.save(commit=False)
            product_object.save()
        
            if stock_form.is_valid():
                stock_object = stock_form.save(commit=False)
                stock_object.product = product_object

                stock_object.save()

        return redirect('home:home')
    

class ProductUpdate(ProductBase, UpdateView):
    template_name = 'CRUDE_Product/update_product.html'
    fields = '__all__'
    model = ProductModel
    title = 'Atualizar Produto'
    success_url = reverse_lazy('product:list-product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ProductDelete(ProductBase, DeleteView):
    template_name = 'CRUDE_Product/delete_product.html'
    model = ProductModel
    title = 'Deletar Produto'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        # breakpoint()
        return context


class ProductSellList(ProductBase, ListView):
    model = ProductModel
    template_name = 'Sell/list_sell_product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context
    

class ProductSell(ProductBase, UpdateView):
    model = ProductModel
    fields = '__all__'
    template_name = 'Sell/sell.html'
    title = "Vender Produto: "

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        product = context['product']

        context['stock_obj'] = StockModel.objects.get(product=product)

        return context

    def post(self, request):
        context = self.get_context_data()
        
        product_form = context['form']
        stock_form = context['form_stock'](self.request.POST)
        breakpoint()

        if product_form.is_valid():
            product_object = product_form.save(commit=False)
            product_object.save()
        
            if stock_form.is_valid():
                stock_object = stock_form.save(commit=False)
                stock_object.product = product_object

                stock_object.save()

        return redirect('home:home')
    