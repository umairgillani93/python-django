from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('task_app.urls')),
    path('aboutus/', include('task_app.urls')),
    path('login/', include('task_app.urls')),
    path('register/', include('task_app.urls')),
    path('questions/', include('task_app.urls')),
    path('choices/', include('task_app.urls')),
    path('admin/', admin.site.urls),
]
