from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("navbar/", views.navbar, name="navbar"),
    path("find_jobs/", views.find_jobs, name="find_jobs"),
    path("job_list/", views.job_list, name="job_list"),
    path("job_details/", views.job_details, name="job_details"),
    # path("employers/", views.employers, name="employers"),
    # path("candidates/", views.candidates, name="candidates"),
    path("blog/", views.blog, name="blog"),
    path("blog_detail/", views.blog_detail, name="blog_detail"),
    path("about/", views.about, name="about"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    # path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
    path("company_dashboard/", views.company_dashboard, name="company_dashboard"),
    path("user_registration/", views.user_registration, name="user_registration"),
    path("company_registration/", views.company_registration, name="company_registration"),
    path("contact/", views.contact, name="contact"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidates-detail/", views.candidatesdetail, name="candidates-detail"),
    path("candidates-list/", views.candidateslist, name="candidates-list"),
    path("Company-list/", views.Companylist, name="Company-list"),
    path("company-detail/", views.companydetail, name="company-detail"),
    path("footer/", views.footer, name="footer"),
    path("error_404/", views.error_404, name="error_404"),
    path("selector/", views.selector, name="selector"),

    #COMPANY DASHBOARD PATHS_______________________
    path("company/company_base_dashboard/", views.company_base_dashboard, name="company_base_dashboard"),
    path("company/company_front_dashboard/", views.company_front_dashboard, name="company_front_dashboard"),
    path("company/company_pending_approval/", views.company_pending_approval, name="company_pending_approval"),
    path("company/company_active_jobs/", views.company_active_jobs, name="company_active_jobs"),
    path("company/company_drafts_jobs/", views.company_drafts_jobs, name="company_drafts_jobs"),
    path("company/company_archived_jobs/", views.company_archived_jobs, name="company_archived_jobs"),
    path("company/company_job_list/", views.company_job_list, name="company_job_list"),
    path("company/company_my_profile/", views.company_my_profile, name="company_my_profile"),
    # path("company/company_post_new_job/", views.company_post_new_job, name="company_post_new_job"),


    #ADMIN DASHBOARD PATHS_______________________
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin/category/", views.company_category, name="company_category"),
    path("admin/companies", views.companies, name="companies"),
    # path("admin/admin_candidate/", views.admin_candidate, name="admin_candidate"),
    # path("admin/admin_package_plan/", views.admin_package_plan, name="admin_package_plan"),
    # path("admin/subscription_list/", views.subscription_list, name="subscription_list"),
    # path("admin/admin_job/", views.admin_job, name="admin_job"),
    # path("admin/admin_applicant/", views.admin_applicant, name="admin_applicant"),
    # path("admin/admin_job_type/", views.admin_job_type, name="admin_job_type"),
    # path("admin/admin_job_skill/", views.admin_job_skill, name="admin_job_skill"),
    # path("admin/admin_category/", views.admin_category, name="admin_category"),
    # path("admin/admin_experience/", views.admin_experience, name="admin_experience"),
    # path("admin/admin_staff/", views.admin_staff, name="admin_staff"),
    # path("admin/admin_role/", views.admin_role, name="admin_role"),
    # path("admin/admin_email/", views.admin_email, name="admin_email"),
    # path("admin/admin_menu/", views.admin_menu, name="admin_menu"),
    # path("admin/admin_frontend/", views.admin_frontend, name="admin_frontend"),
    



    path("candidate/candidate_base/", views.candidate_base, name="candidate_base"),
    path("candidate/candidate_front_dashboard/", views.candidate_front_dashboard, name="candidate_front_dashboard"),
    path("candidate/candidate_edit_profile/", views.candidate_edit_profile, name="candidate_edit_profile"),
    path("candidate/bookmark_jobs/", views.bookmark_jobs, name="bookmark_jobs"),
    path("candidate/applied_jobs/", views.applied_jobs, name="applied_jobs"),
    path("candidate/candidate_edit_resume/", views.candidate_edit_resume, name="candidate_edit_resume"),
    path("candidate/job_alert/", views.job_alert, name="job_alert"),
    path("candidate/candidate_notifications/", views.candidate_notifications, name="candidate_notifications"),
    path("candidate/candidate_view_resume/", views.candidate_view_resume, name="candidate_view_resume"),
    
]

