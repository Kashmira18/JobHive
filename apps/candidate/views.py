from django.shortcuts import render
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, "candidate/candidate_dashboard.html")
def dashboard(request):
    return render(request, "candidate/dashboard.html")
