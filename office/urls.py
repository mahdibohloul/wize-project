from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('apply', views.apply, name='apply'),
    path('notifications', include('notifications.urls')),
    path('task', include('task.urls')),
    path('is_done', views.is_done, name='is_done'),

]