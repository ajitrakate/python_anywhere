from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views import generic

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('<int:pk>/', views.buttons, name='buttons'),
    path('<int:pk>/<int:id>/', views.change_status, name='change_status')
]