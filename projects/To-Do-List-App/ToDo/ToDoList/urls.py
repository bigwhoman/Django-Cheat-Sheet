from django.urls import path, include
from . import views

app_name = 'ToDoList'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index')
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
]
