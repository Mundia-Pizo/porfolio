from django.shortcuts import render
from django.views.generic import ListView
from .models import Projects

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def home(request):
    return render(request, "core/index.html")

def work(request):
    return render(request, "core/work.html")


class ProjectView(ListView):
	model =Projects
	template_name="core/project.html"
