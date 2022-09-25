from django.contrib import admin
from django.urls import path, include
from .views import weather_search_view

urlpatterns = [
    path("", weather_search_view, name='weather_search_view')
]