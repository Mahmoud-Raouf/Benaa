from django.shortcuts import redirect, render
from accounts.models import Company
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from request.forms import RequestForm
from .models import *
from django.contrib.auth.decorators import login_required



#  Consultation Start Request
@login_required
def request_list(request):
    request_list  = ConsultationRequest.objects.all()

    return render(request ,'consultation_request/my_request_list.html', {
        'request_list' : request_list ,
        'title' : 'كل طلبات الاستشارة',

    })
    
@login_required 
def comment_display(request , id):
    
    consultationid  = get_object_or_404(ConsultationRequest, id=id)
    try:
        comment_display = ConsultationComment.objects.get(consultationrequest=consultationid)
    except ConsultationComment.DoesNotExist:
        comment_display = None 

    return render(request ,'consultation_request/comment_display.html', {
        'consultationid' : consultationid ,
        'comment_display' : comment_display ,
        'title' : 'الرد الخاص بإستشارتك',

    })
    
@login_required 
def add_request(request ,id=id):
    company = Company.objects.get(id = id)
    request_form = RequestForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        request_form = RequestForm(request.POST or None , request.FILES)
        if request_form.is_valid():
            check_user_request = request_form.save(commit=False)
            check_user_request.company = company
            check_user_request.user = request.user
            check_user_request.save()
            return redirect('dashboard:dashboard')

    else:
        request_form = RequestForm()
    return render(request ,'consultation_request/add_request.html', {
        'request_form' : request_form ,
        'title' : 'اضافة طلب إستشارة',
    })
    

@login_required
def add_comment_to_ConsultationRequest(request, pk):

    consultationrequest = get_object_or_404(ConsultationRequest, pk=pk)
    comment =consultationrequest.company

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.consultationrequest = consultationrequest
            comment.author = request.user
            comment.save()
            return redirect("orders:request_order_for_company")

    else:
        form = CommentForm()
    return render(request, 'consultation_request/add_consultation_comment.html', {'form': form,'comment': comment})

    
    
    
@login_required 
def request_delete(request , pk):
    request_delete = ConsultationRequest.objects.get(pk=pk)
    request_delete.delete()
    return redirect('request:user_request_consultation_list')

# end  Consultation Request





# Start Request Project



@login_required
def project_request_list(request):
    user_companies = Company.objects.filter(user=request.user)
    project_request_list = ProjectRequest.objects.filter(company__in=user_companies)

    return render(request ,'project_request/my_project_request.html', {
        'project_request_list': project_request_list,
        'title' : 'طلبيات المشاريع',

    })
    
    
# def comment_Project_display(request , id):
#     projectRequest  = get_object_or_404(ProjectRequest, id=id)
#     comment_Project_display = ConsultationComment.objects.get(consultationrequest=projectRequest)


#     return render(request ,'consultation_request/display_comment.html', {
#         'projectRequest' : projectRequest ,
#         'comment_Project_display' : comment_Project_display ,
#         'title' : 'الطلبات',

#     })
    
@login_required 
def add_Project_Request(request ,id=id):
    company = Company.objects.get(id = id)
    request_form = ProjectRequestForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        request_form = ProjectRequestForm(request.POST or None , request.FILES)
        if request_form.is_valid():
            check_user_request = request_form.save(commit=False)
            check_user_request.company = company
            check_user_request.user = request.user
            check_user_request.save()
            return redirect('users:company_list')

    else:
        request_form = ProjectRequestForm()
    return render(request ,'project_request/add_Project_Request.html', {
        'request_form' : request_form ,
        'title' : 'إضافة طلب مشروع',
    })
    

@login_required
def add_Update_Project_Status(request, id):
    projectRequestId = get_object_or_404(ProjectRequest, pk=id)
    try:
        projectStatus = ProjectStatus.objects.get(projectrequest=projectRequestId)
    except ProjectStatus.DoesNotExist:
        projectStatus = None

    if request.method == 'POST':
        form = ProjectStatusForm(request.POST, request.FILES, instance=projectStatus)
        if form.is_valid():
            projectStatus = form.save(commit=False)
            projectStatus.projectrequest = projectRequestId
            projectStatus.save()
            return redirect('request:project_request_list')  
    else:
        form = ProjectStatusForm(instance=projectStatus)
    return render(request, 'project_request/add_Update_Project_Status.html', {'form': form})
    








@login_required 
def add_Contracts_Guarantees(request, id):
    projectRequestId = get_object_or_404(ProjectRequest, pk=id)
    try:
        contractsguarantees = Contracts_Guarantees.objects.get(contracts_guarantees=projectRequestId)
    except Contracts_Guarantees.DoesNotExist:
        contractsguarantees = None

    if request.method == 'POST':
        form = Contracts_GuaranteesForm(request.POST, request.FILES, instance=contractsguarantees)
        if form.is_valid():
            contractsguarantees = form.save(commit=False)
            contractsguarantees.contracts_guarantees = projectRequestId
            contractsguarantees.save()
            return redirect('request:project_request_list')  # Replace 'request:project_request_list' with the appropriate URL for your project request list view

    else:
        form = Contracts_GuaranteesForm(instance=contractsguarantees)

    return render(request, 'project_request/add_Contracts_Guarantees.html', {'form': form})
    

















@login_required  
def add_Project_Meetings(request, id):
    projectrequestId = get_object_or_404(ProjectRequest, pk=id)
    try:
        projectmeetings = ProjectMeetings.objects.get(project_meetings=projectrequestId)
    except ProjectMeetings.DoesNotExist:
        projectmeetings = None

    if request.method == 'POST':
        form = ProjectMeetingsForm(request.POST, instance=projectmeetings)
        if form.is_valid():
            projectmeetings = form.save(commit=False)
            projectmeetings.project_meetings = projectrequestId
            projectmeetings.save()
            return redirect('request:project_request_list')  # Replace 'request:project_request_list' with the appropriate URL for your project request list view

    else:
        form = ProjectMeetingsForm(instance=projectmeetings)
    return render(request, 'project_request/add_Project_Meetings.html', {'form': form})
    
    
    
@login_required 
def request_delete(request , pk):
    request_delete = ConsultationRequest.objects.get(pk=pk)
    request_delete.delete()
    return redirect('project_request:request_list')

# end Request Project