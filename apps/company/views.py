from django.shortcuts import render
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, "company/base.html")
def signup(request):
    return render(request, "company/signup.html")
def dashboard(request):
    return render(request, "company/dashboard.html")