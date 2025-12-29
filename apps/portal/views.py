from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import CustomUser
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required

from apps.common.decorators import role_required  # create decorator of role required


# from django.contrib.auth.forms import UserCreationForm
# from .forms import UserProfileForm


def home(request):
    return render(request, "portal/home.html")

def selector(request):
    return render(request, "portal/selector.html")

def navbar(request):
    return render(request, "portal/navbar.html")


def footer(request):
    return render(request, "portal/footer.html")


def about(request):
    return render(request, "portal/about.html")


def find_jobs(request):
    return render(request, "portal/find_jobs.html")


def job_list(request):
    return render(request, "portal/job_list.html")


def job_details(request):
    return render(request, "portal/job_details.html")


# def employers(request):
#     return render(request, "portal/employers.html")


def blog(request):
    return render(request, "portal/blog.html")


def blog_detail(request):
    return render(request, "portal/blog_detail.html")


def candidates(request):
    return render(request, "portal/candidates.html")


def contact(request):
    return render(request, "portal/contact.html")


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.role == "admin":
                    return redirect("admin_dashboard")
                elif user.role == "company":
                    return redirect("company_dashboard")

                else:
                    return redirect("user_dashboard")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Form Errors")
    else:
        form = LoginForm()

    return render(request, "portal/signin.html", {"form": form})

# def user_dashboard(request):
#     return render(request, "portal/user_dashboard.html", {})


# def logoutUser(request):
#     logout(request)
#     return redirect("login")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            messages.success(request, "Account Created Successfully! Please Login")
            # return redirect("login")
            user_type = int(form.cleaned_data["user_type"])

            if user_type == 1:  # Candidate
                return redirect("user_registration")
            elif user_type == 2:
                return redirect("company_registration")

            return redirect("/")
        else:
            messages.error(request, "Please Correct the errors below.")
    else:
        form = SignupForm()
    return render(request, "portal/signup.html", {"form": form})


# @login_required
def user_registration(request):
    return render(request, "portal/user_registration.html")


def company_dashboard(request):
    return render(request, "portal/company_dashboard.html")


def company_registration(request):
    return render(request, "portal/company_registration.html")


# def candidates(request):
#     return render(request, "portal/candidates.html")


def candidatesdetail(request):
    return render(request, "portal/candidates-detail.html")


def candidateslist(request):
    return render(request, "portal/candidates-list.html")


def Companylist(request):
    return render(request, "portal/Company-list.html")


def companydetail(request):
    return render(request, "portal/company-detail.html")


def error_404(request):
    return render(request, "portal/error_404.html")

# COMPANY DASHBOARD VIEWS_______________________
def company_base_dashboard(request):
    return render(request, "portal/company/company_base_dashboard.html")

def company_front_dashboard(request):
    return render(request, "portal/company/company_front_dashboard.html")

# ADMIN DASHBOARD VIEWS_______________________
# @role_required(["admin"])
# @role_required(allowed_roles=["admin"])
def admin_dashboard(request):
    return render(request, "portal/admin/admin_dashboard.html")

def admin_company_type(request):
    return render(request, "portal/admin/admin_company_type.html")

def admin_package_plan(request):
    return render(request, "portal/admin/admin_package_plan.html")

def subscription_list(request):
    return render(request, "portal/admin/subscription_list.html")

def admin_candidate(request):
    return render(request, "portal/admin/admin_candidate.html")

def admin_company(request):
    return render(request, "portal/admin/admin_company.html")

def admin_job(request):
    return render(request, "portal/admin/admin_job.html")

def admin_applicant(request):
    return render(request, "portal/admin/admin_applicant.html")

def admin_category(request):
    return render(request, "portal/admin/admin_category.html")

def admin_job_type(request):
    return render(request, "portal/admin/admin_job_type.html")

def admin_job_skill(request):
    return render(request, "portal/admin/admin_job_skill.html")

def admin_experience(request):
    return render(request, "portal/admin/admin_experience.html")

def admin_staff(request):
    return render(request, "portal/admin/admin_staff.html")

def admin_role(request):
    return render(request, "portal/admin/admin_role.html")

def admin_menu(request):
    return render(request, "portal/admin/admin_menu.html")

def admin_frontend(request):
    return render(request, "portal/admin/admin_frontend.html")

def admin_email(request):
    return render(request, "portal/admin/admin_email.html")