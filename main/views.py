from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # Baad mein database mein save karein ge!
    return render(request, 'contact.html')