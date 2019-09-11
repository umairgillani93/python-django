from django.urls import path
from MTV_app import views

urlpatterns = [
    path('', views.index, name = 'index')
]
