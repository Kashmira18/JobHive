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
    path("forgotpassword/", views.forgotpassword, name="forgotpassword"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
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
    # path("post_job/", views.post_job, name="post_job"),


    #COMPANY DASHBOARD PATHS_______________________
    path("company/company_dashboard/", views.company_dashboard, name="company_dashboard"),
    path("company/first_page/", views.first_page, name="first_page"),
    # path("company/front/", views.front, name="front"),
    path("company/active/", views.active, name="active"),
    path("company/drafts/", views.drafts, name="drafts"),
    path("company/job_lists/", views.job_lists, name="job_lists"),
    path("company/profile/", views.profile, name="profile"),
    path("company/messenger/", views.messenger, name="messenger"),
    # path("company/post_job/", views.post_job, name="post_job"),
    path("company/company_job_post/", views.company_job_post, name="company_job_post"),
    # path("company/logout/", views.logout_view, name="logout_view"),
    path("company/setting/", views.setting, name="setting"),

    #ADMIN DASHBOARD PATHS_______________________
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin/category/", views.company_category, name="company_category"),
    path("admin/companies", views.companies, name="companies"),
    path("admin/candidate", views.candidate, name="candidate"),
    path("admin/packages/", views.packages, name="packages"),
    path("admin/subscription/", views.subscription, name="subscription"),
    path("admin/job/", views.job, name="job"),
    path("admin/applicant/", views.applicant, name="applicant"),
    path("admin/job_type/", views.job_type, name="job_type"),
    path("admin/admin_category/", views.admin_category, name="admin_category"),
    path("admin/job_skill/", views.job_skill, name="job_skill"),
    path("admin/experience/", views.experience, name="experience"),
    path("admin/staff/", views.staff, name="staff"),
    path("admin/role/", views.role, name="role"),
    path("admin/email/", views.email, name="email"),
    path("admin/menu/", views.menu, name="menu"),


    # CANDIDATE DASHBOARD PATHS_______________________
    path("candidate/candidate_base/", views.candidate_base, name="candidate_base"),
    path("candidate/candidate_front_dashboard/", views.candidate_front_dashboard, name="candidate_front_dashboard"),
    path("candidate/candidate_edit_profile/", views.candidate_edit_profile, name="candidate_edit_profile"),
    path("candidate/bookmark_jobs/", views.bookmark_jobs, name="bookmark_jobs"),
    path("candidate/applied_jobs/", views.applied_jobs, name="applied_jobs"),
    path("candidate/candidate_edit_resume/", views.candidate_edit_resume, name="candidate_edit_resume"),
    path("candidate/job_alert/", views.job_alert, name="job_alert"),
    path("candidate/candidate_notifications/", views.candidate_notifications, name="candidate_notifications"),
    path("candidate/candidate_view_resume/", views.candidate_view_resume, name="candidate_view_resume"),
    



    path("candidate/candidate_base/", views.candidate_base, name="candidate_base"),
    path("candidate/candidate_front_dashboard/", views.candidate_front_dashboard, name="candidate_front_dashboard"),
    path("candidate/candidate_edit_profile/", views.candidate_edit_profile, name="candidate_edit_profile"),
    path("candidate/bookmark_jobs/", views.bookmark_jobs, name="bookmark_jobs"),
    path("candidate/applied_jobs/", views.applied_jobs, name="applied_jobs"),
    path("candidate/candidate_edit_resume/", views.candidate_edit_resume, name="candidate_edit_resume"),
    path("candidate/job_alert/", views.job_alert, name="job_alert"),
    path("candidate/candidate_notifications/", views.candidate_notifications, name="candidate_notifications"),
    path("candidate/candidate_view_resume/", views.candidate_view_resume, name="candidate_view_resume"),
    path("candidate/setting/", views.candidate_setting, name="candidate_setting"),

    
]


