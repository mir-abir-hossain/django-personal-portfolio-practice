from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

# Create your views here.
def home(request):
    ops = Project.objects.first()
    return render(request, template_name='portfolio/home.html', context={'testingg':ops})
