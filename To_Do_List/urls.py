from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_do_list, name='to_do_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]
