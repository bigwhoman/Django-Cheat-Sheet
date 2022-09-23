from django.urls import path

from . import views

app_name = 'shortner'  # Namespacing to differentiate URL names between Django apps

# generic views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('shortner/create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]
