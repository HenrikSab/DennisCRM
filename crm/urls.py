from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [

    path('', views.home),
    path('customers/', views.customers),
    path('products/', views.products),
    path('dashboard/', views.dashboard),

]
