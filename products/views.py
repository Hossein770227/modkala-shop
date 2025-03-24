from django.shortcuts import render
from django.views.generic import TemplateView

class Product_list(TemplateView):
    template_name = 'products/product_list.html'