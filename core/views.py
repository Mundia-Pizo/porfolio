from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, MyWork

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def home(request):
    return render(request, "core/index.html")

class Work(ListView):
    model = MyWork
    template_name = "core/work.html"

class WorkDetailView(DetailView):
    model = MyWork
    template_name = "core/work_detail.html"

class ProjectView(DetailView):
	model = Project
	template_name="core/project.html"
