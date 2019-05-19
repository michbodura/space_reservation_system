from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('', views.forgot_password, name='forgot_password'),
    path('', views.register, name='register'),
]