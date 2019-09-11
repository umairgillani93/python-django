from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('formspage/', views.forms_name_view, name = 'forms_name_view')
]
