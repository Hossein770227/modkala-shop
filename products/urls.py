from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Product_list.as_view(), name='product_list'),
]
