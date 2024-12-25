from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Начальная страница
    path('tasks/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.custom_logout, name='logout'),  # Собственный маршрут для выхода
]