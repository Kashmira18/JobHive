from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("navbar/", views.navbar, name="navbar"),
    path("find_jobs/", views.find_jobs, name="find_jobs"),
    path("job_list/", views.job_list, name="job_list"),
    path("job_details/", views.job_details, name="job_details"),
    path("employers/", views.employers, name="employers"),
    path("candidates/", views.candidates, name="candidates"),
    path("blog/", views.blog, name="blog"),
    path("blog_detail/", views.blog_detail, name="blog_detail"),
    path("about/", views.about, name="about"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
    path("company_dashboard/", views.company_dashboard, name="company_dashboard"),
    path("user_registration/", views.user_registration, name="user_registration"),
    path(
        "company_registration/", views.company_registration, name="company_registration"
    ),
    path("contact/", views.contact, name="contact"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidates-detail/", views.candidatesdetail, name="candidates-detail"),
    path("candidates-list/", views.candidateslist, name="candidates-list"),
    path("Company-list/", views.Companylist, name="Company-list"),
    path("company-detail/", views.companydetail, name="company-detail"),
    path("footer/", views.footer, name="footer"),
]
