from django.urls import path
from . import views

app_name = 'company'  # This defines the namespace

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
