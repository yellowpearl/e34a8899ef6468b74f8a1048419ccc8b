from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_func),
    path('main', views.main),
    ]