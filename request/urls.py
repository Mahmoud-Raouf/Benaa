from django.urls import path
from . import views
app_name = 'request'

urlpatterns = [


    # Start Request
    path('request/' , views.request_list, name= 'request_list'),
    path('add_request/<int:id>/' , views.add_request, name= 'add_request'),
    path('request_delete/<int:pk>/' , views.request_delete, name= 'request_delete'),
    # end Request
    path('request/<int:pk>/comment/', views.add_comment_to_ConsultationRequest, name='add_comment_to_ConsultationRequest'),
    path('request/<int:id>/comment_display/', views.comment_display, name='comment_display'),
    
    # Start Project Request
    path('project_request_list/' , views.project_request_list, name= 'project_request_list'),
    path('add_Project_Request/<int:id>/' , views.add_Project_Request, name= 'add_Project_Request'),
    path('add_Update_Project_Status/<int:id>/' , views.add_Update_Project_Status, name= 'add_Update_Project_Status'),
    path('add_Contracts_Guarantees/<int:id>/' , views.add_Contracts_Guarantees, name= 'add_Contracts_Guarantees'),
    path('add_Project_Meetings/<int:id>/' , views.add_Project_Meetings, name= 'add_Project_Meetings'),

    
    
    # End Project Request

]