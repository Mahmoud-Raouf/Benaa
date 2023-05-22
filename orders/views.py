from django.shortcuts import get_object_or_404, render

from request.models import *


def request_order_for_company(request):
    request_order_for_company  = ConsultationRequest.objects.filter(user = request.user)

    return render(request ,'request_order_for_company.html', {
        'request_order_for_company' : request_order_for_company ,
        'title' : 'طلبات الإستشارة الخاصة بك',

    })

def project_request_orders(request):
    project_request_orders  = ProjectRequest.objects.filter(user = request.user)

    return render(request ,'project_request_orders.html', {
        'project_request_orders' : project_request_orders ,
        'title' : 'طلبيات مشاريعك',

    })


def project_status(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)

    project_status  = ProjectStatus.objects.get(projectrequest = ProjectRequestid)

    return render(request ,'project_status.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'project_status' : project_status ,
        'title' : 'حالة المشروع الخاص بك',

    })

def project_Steps(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)
    project_status  = ProjectStatus.objects.get(projectrequest = ProjectRequestid)

    return render(request ,'project_Steps_liner.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'project_status' : project_status ,
        'title' : 'مراحل المشروع',

    })


def contracts_guarantees(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)

    contracts_guarantees  = Contracts_Guarantees.objects.get(contracts_guarantees = ProjectRequestid)

    return render(request ,'contracts_guarantees.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'contracts_guarantees' : contracts_guarantees ,
        'title' : 'حالة المشروع الخاص بك',

    })


def project_meetings(request , id):
    ProjectRequestid  = get_object_or_404(ProjectRequest, id=id)

    project_meetings  = ProjectMeetings.objects.get(project_meetings = ProjectRequestid)

    return render(request ,'project_meetings.html', {
        'ProjectRequestid' : ProjectRequestid ,
        'project_meetings' : project_meetings ,
        'title' : 'حالة المشروع الخاص بك',

    })


