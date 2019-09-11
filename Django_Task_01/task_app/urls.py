from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('questions', views.question_list, name = 'question_list'),
    path('choices/', views.choice_list, name = 'choice_list')
]
