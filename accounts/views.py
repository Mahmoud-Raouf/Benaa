from django.shortcuts import redirect, render
from django.shortcuts import render ,redirect
from .forms import UserForm
from django.contrib.auth import authenticate , login
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CompanyForm
from .models import Company, Profile

# Start company
def company_list(request):
    company_list  = Company.objects.filter(company_request = True)

    return render(request ,'company/company_list.html', {
        'company_list' : company_list ,
        'title' : 'كل الشركات',

    })
    
    
    
    
def outstanding_companies(request):
    outstanding_companies  = Company.objects.filter(company_request = False)

    if 'Companyupdate' in request.POST :
        if request.user.is_authenticated:
            CompanyId = request.POST.get('CompanyId')

            CompanyItem= Company.objects.get(id=CompanyId)
            CompanyItem.company_request = True
            CompanyItem.save()
            
    if 'Companydelete' in request.POST :
        if request.user.is_authenticated:
            CompanyId = request.POST.get('CompanyId')

            requesItem= Company.objects.get(id=CompanyId)
            requesItem.delete()
            
            
    return render(request ,'company/outstanding_companies.html', {
        'outstanding_companies' : outstanding_companies ,
        'title' : 'الشركات المعلقة',

    })
    
    
    
    
def accepted_companies(request):
    accepted_companies  = Company.objects.filter(company_request = True)

    return render(request ,'company/accepted_companies.html', {
        'accepted_companies' : accepted_companies ,
        'title' : 'الشركات المقبولة',

    })
    
    
def add_company(request):
    company_form = CompanyForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        company_form = CompanyForm(request.POST or None , request.FILES)
        if company_form.is_valid():
            check_user_company = company_form.save(commit=False)
            check_user_company.user = request.user
            check_user_company.save()
            return redirect('company:company_list')

    else:
        company_form = CompanyForm()
    return render(request ,'company/add_company.html', {
        'company_form' : company_form ,
        'title' : 'إضافة طلب',

    })
    
    
    
    
def company_delete(request , pk):
    company_delete = Company.objects.get(pk=pk)
    company_delete.delete()
    return redirect('company:company_list')
# end company


# Start Auth
def users(request):
    users  = User.objects.all()

    return render(request ,'registration/users.html', {
        'users' : users ,
        'title' : 'العملاء',

    })
    
    
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password2']
            user = authenticate(request , username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect('dashboard:dashboard')
    else:
        form =UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form' : form ,
    })



def user_login(request):

    if request.method == 'POST':
        login_form = UserForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('dashboard:dashboard')
    else:
        login_form = UserForm()
        
    return render(request , 'registration/login.html' , {
        'login_form' : login_form
    })


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')
# End Auth

def project_Steps(request):

    return render(request ,'company/project_Steps_liner.html', {
        'title' : 'العملاء',

    })