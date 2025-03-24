from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('signup/', views.UserRegisterView.as_view(), name='user_register'),
    path('verify/', views.UserRegisterCodeView.as_view(),name='verify_code'),
    path('login/', views.login_view,name='login'),
    path('change_password/', views.password_change_view,name='change_password'),
]
