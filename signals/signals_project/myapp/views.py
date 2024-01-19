from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def create_instance_view(request):
    instance = MyModel(name="suraj")
    instance.save()
    return HttpResponse("record added successfully")


