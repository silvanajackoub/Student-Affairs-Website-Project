from django.urls import path
from . import views


urlpatterns = [
    # pages of the website
    path('', views.home, name='home'),  # for the home page --> Default page when we run the server
    path('contact-us/', views.contact, name='contact'),
    path('department/', views.dept, name='dept'),  # department assignment page
    path('update/', views.table_view, name='update'),  # edit-delete table page
    path('registraion/', views.regist, name='regist'),  # add student page
    path('search/', views.search, name='search'),  # student search page
    path('sign-up/', views.sign_up, name='sign-up'),  # sign up page
    path('login/', views.log_in, name='affairs-home'),  # login page (or student affairs home)

    # urls that call functional views
    path('logout/', views.log_out, name="log-out"),  # calls the log_out view to log a user out
    path('get_search/', views.get_search, name='get_search'),  # calls the get_search used in the search page
    path('get_update/', views.get_update, name='get_update'),  # calls get_update used in the edit-delete page
    path('del_student/', views.del_student, name='del_student'),  # calls del_student used in the edit-delete page
    path('edit_student/', views.edit_student, name='edit_student'),  # calls edit_student used in the edit-delete page
]
