from django.urls import path
from Basics import views

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('hello1/', views.index1, name = 'index1'),
    path('login1/', views.login1, name = 'login1'),
    path('register1/', views.register1, name = 'register1')
]
