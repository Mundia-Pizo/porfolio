from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, MyWork, ProfilePicture

def about(request):
    profile = ProfilePicture.objects.all()

    context = {
        'profile':profile
    }
    return render(request, "core/about.html", context)

def contact(request):
    profile = ProfilePicture.objects.all()
    context={
        'profile':profile
    }
    return render(request, "core/contact.html",context)

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
