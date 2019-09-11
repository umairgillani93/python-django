from django.urls import path
from models_app import views

urlpatterns = [
    path('', views.index, name = 'index')
]
