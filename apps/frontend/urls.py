from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('register_function', views.register_function),
    path('login_function', views.login_function),
    path('dashboard', views.dashboard),

]