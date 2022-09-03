from django.urls import path

from . import views

urlpatterns = [
    path('home', views.simple_view, name='simple_view'),
]