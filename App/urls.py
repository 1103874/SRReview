from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.SRCreate, name='SRCreate'),
    path('delete/<int:qs_id>', views.SRDelete, name='SRDelete'),
    path('update/<int:qs_id>', views.SRUpdate, name='SRUpdate'),
]