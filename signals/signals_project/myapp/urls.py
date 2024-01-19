
# myapp/urls.py
from django.urls import path
from .views import create_instance_view

urlpatterns = [
    path('create_instance/', create_instance_view, name='create_instance'),
]
