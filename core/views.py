from django.shortcuts import render
from django.views.generic import ListView

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def home(request):
    return render(request, "core/index.html")

def work(request):
    return render(request, "core/work.html")
