from django.urls import path
from games import views 

# app_name = 'blog'

urlpatterns = [
    path('', views.games, name= 'games'),
]