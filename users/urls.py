from django.urls import path, include
from . import views #dot means the same folder 

app_name = 'users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
]