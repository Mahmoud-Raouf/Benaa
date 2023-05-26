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
        'title' : 'الطلبات',

    })
    
@login_required 
def comment_display(request , id):
    consultationid  = get_object_or_404(ConsultationRequest, id=id)
    comment_display = ConsultationComment.objects.get(consultationrequest=consultationid)


    return render(request ,'consultation_request/display_comment.html', {
        'consultationid' : consultationid ,
        'comment_display' : comment_display ,
        'title' : 'الطلبات',

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
            return redirect('request:request_list')

    else:
        request_form = RequestForm()
    return render(request ,'consultation_request/add_request.html', {
        'request_form' : request_form ,
        'title' : 'إضافة طلب إستشارة',
    })
    

@login_required
def add_comment_to_ConsultationRequest(request, pk):
    product = get_object_or_404(ConsultationRequest, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'consultation_request/add_consultation_comment.html', {'form': form})
    
    
    
@login_required 
def request_delete(request , pk):
    request_delete = ConsultationRequest.objects.get(pk=pk)
    request_delete.delete()
    return redirect('request:request_list')

# end  Consultation Request





# Start Request Project
@login_required
def project_request_list(request):
    project_request_list  = ProjectRequest.objects.filter(user = request.user)

    return render(request ,'project_request/my_project_request.html', {
        'project_request_list' : project_request_list ,
        'title' : 'طلبات المشاريع',

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
            return redirect('request:request_list')

    else:
        request_form = ProjectRequestForm()
    return render(request ,'project_request/add_Project_Request.html', {
        'request_form' : request_form ,
        'title' : 'إضافة طلب مشروع',
    })
    

@login_required
def add_Update_Project_Status(request, id):
    projectstatusId = get_object_or_404(ProjectRequest, pk=id)
    form = ProjectStatusForm(request.POST, request.FILES)

    if request.method == 'POST':
        form = ProjectStatusForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.projectstatus = projectstatusId
            comment.save()
    else:
        form = ProjectStatusForm()
    return render(request, 'project_request/add_Update_Project_Status.html', {'form': form})
    
@login_required 
def add_Contracts_Guarantees(request, id):
    projectstatusId = get_object_or_404(ProjectRequest, pk=id)
    if request.method == 'POST':
        form = Contracts_GuaranteesForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.contracts_guarantees = projectstatusId
            comment.save()
    else:
        form = Contracts_GuaranteesForm()
    return render(request, 'project_request/add_Contracts_Guarantees.html', {'form': form})
    
    
@login_required  
def add_Project_Meetings(request, id):
    projectstatusId = get_object_or_404(ProjectRequest, pk=id)
    if request.method == 'POST':
        form = ProjectMeetingsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.contracts_guarantees = projectstatusId
            comment.save()
    else:
        form = ProjectMeetingsForm()
    return render(request, 'project_request/add_Project_Meetings.html', {'form': form})
    
    
    
@login_required 
def request_delete(request , pk):
    request_delete = ConsultationRequest.objects.get(pk=pk)
    request_delete.delete()
    return redirect('project_request:request_list')

# end Request Project