from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create, name='create'),
    path('chart/', views.chart, name='chart'),
]