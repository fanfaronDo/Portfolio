from django.shortcuts import render
from .models import Project
import datetime


def main_page(requests):
    projects = Project.objects.all()
    date = datetime.datetime.now()
    return render(requests, 'portfolio/home.html', {'projects': projects, "datetime": date})
