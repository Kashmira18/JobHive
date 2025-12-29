from django.urls import path
from . import views

app_name = 'candidate'  # This defines the namespace

urlpatterns = [
    path("", views.home, name="home"),
    # path("find_jobs/", views.find_jobs, name="find_jobs"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
