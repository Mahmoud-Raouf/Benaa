from django.shortcuts import get_object_or_404, render
from request.models import *
from django.contrib.auth.decorators import login_required



@login_required
def request_order_for_company(request):
    company = Company.objects.get(user = request.user)    
    request_order_for_company  = ConsultationRequest.objects.filter(company = company)

    return render(request ,'request_order_for_company.html', {
        'request_order_for_company' : request_order_for_company ,
        'title' : 'طلبات إستشارة العملاء',

    })

@login_required
def user_request_consultation_list(request):
    user_request_consultation_list  = ConsultationRequest.objects.filter(user = request.user)

    return render(request ,'user_request_consultation_list.html', {
        'user_request_consultation_list' : user_request_consultation_list ,
        'title' : 'طلبات الإستشارة الخاصة بك',

    })

@login_required
def project_request_list(request):
    project_request_list  = ProjectRequest.objects.all()

    return render(request ,'project_request_list.html', {
        'project_request_list' : project_request_list ,
        'title' : 'كل المشاريع',

    })
@login_required
def project_request_orders(request):
    project_request_orders  = ProjectRequest.objects.filter(user = request.user)

    return render(request ,'project_request_orders.html', {
        'project_request_orders' : project_request_orders ,
        'title' : 'طلبيات مشاريعك',

    })

@login_required
def project_status(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)

    project_status  = ProjectStatus.objects.get(projectrequest = ProjectRequestid)

    return render(request ,'project_status.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'project_status' : project_status ,
        'title' : 'حالة المشروع الخاص بك',

    })

@login_required
def project_Steps(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)
    project_status  = ProjectStatus.objects.get(projectrequest = ProjectRequestid)

    return render(request ,'project_Steps_liner.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'project_status' : project_status ,
        'title' : 'مراحل المشروع',

    })

@login_required
def contracts_guarantees(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)

    contracts_guarantees  = Contracts_Guarantees.objects.get(contracts_guarantees = ProjectRequestid)

    return render(request ,'contracts_guarantees.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'contracts_guarantees' : contracts_guarantees ,
        'title' : 'حالة المشروع الخاص بك',

    })

@login_required
def project_meetings(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)

    project_meetings  = ProjectMeetings.objects.get(project_meetings = ProjectRequestid)

    return render(request ,'project_meetings.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'project_meetings' : project_meetings ,
        'title' : 'حالة المشروع الخاص بك',

    })


