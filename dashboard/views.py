from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.models import Company, Profile
from django.contrib.auth.decorators import login_required


from request.models import ConsultationRequest, ProjectRequest


@login_required
def dashboard(request):

    Company_sum = Company.objects.all().count()
    pending_company = Company.objects.filter(company_request = False).count()
    accepted_company = Company.objects.filter(company_request = True).count()
    User_sum = User.objects.all().count()
    User_request_list  = ConsultationRequest.objects.filter(user = request.user).count()
    Consultation_count  = ConsultationRequest.objects.all().count()
    Project_count  = ProjectRequest.objects.all().count()
    user_profile = Profile.objects.get(user=request.user)


    return render(request , 'dashboard.html' , {
        'Company_sum' : Company_sum ,
        'User_sum' : User_sum,
        'user_profile' : user_profile,
        'pending_company' : pending_company,
        'accepted_company' : accepted_company,
        'User_request_list' : User_request_list,
        'Consultation_count' : Consultation_count,
        'Project_count' : Project_count,
    })
