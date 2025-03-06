from django.shortcuts import render


def home(request):
    return render(request , "core/home.html")

def about(request):
    return render(request , "core/about.html")

def contact(request):
    return render(request , "core/contact.html")

def login_user(request):
    return render(request , "core/login_user.html")

def register_user(request):
    return render(request , "core/register_user.html")
