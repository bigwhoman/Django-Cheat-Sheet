from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'dictionary'
urlpatterns = [
    path("", views.index, name='index'),
    path("dictionary/search", views.search, name='search'),
]
