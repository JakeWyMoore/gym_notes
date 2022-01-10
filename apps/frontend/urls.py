from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('register_function', views.register_function),
    path('login_function', views.login_function),
    path('dashboard', views.dashboard),

    path('create-workout', views.create_workout),
    path('create-workout-logic', views.create_workout_logic),


]