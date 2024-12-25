from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Маршруты для аутентификации
    path('', include('tasks.urls')),  # Маршруты для вашего приложения
]