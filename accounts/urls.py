from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [


    # Start company
    path('company/' , views.company_list, name= 'company_list'),
    path('outstanding_companies/' , views.outstanding_companies, name= 'outstanding_companies'),
    path('accepted_companies/' , views.accepted_companies, name= 'accepted_companies'),
    path('add_company/' , views.add_company, name= 'add_company'),
    path('company_delete/<int:pk>/' , views.company_delete, name= 'company_delete'),
    # end company
    
    # Start Auth
    path('users/' , views.users, name='users'),
    path('company_users/' , views.company_users, name='company_users'),
    path('profile/' , views.profile, name='profile'),
    path('signup/' , views.signup, name='signup'),
    path('login/' , views.user_login, name='login'),
    path('logout/' , views.logout, name='logout'),
    # end Auth


]