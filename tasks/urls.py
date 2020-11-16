from django.urls import path

from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('task/', views.taskList, name='tasklist'),
    path('', views.login),
    path('list/', views.taskList, name='tasklist'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]