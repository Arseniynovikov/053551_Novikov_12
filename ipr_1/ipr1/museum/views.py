from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def contacts(request):
    return  render(request, "contacts.html")

def exhibits(request):
    return render(request, "exhibits.html")

def schedule(request):
    return render(request, "schedule.html")
