from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('request_order_for_company/' , views.request_order_for_company  , name='request_order_for_company'),
    path('user_request_consultation_list/' , views.user_request_consultation_list  , name='user_request_consultation_list'),
    path('project_request_list/' , views.project_request_list  , name='project_request_list'),

    path('project_request_orders/' , views.project_request_orders  , name='project_request_orders'),
    path('project_request_delete/<int:pk>/' , views.project_request_delete  , name='project_request_delete'),

    path('<int:id>/project_status/' , views.project_status  , name='project_status'),
    path('<int:id>/contracts_guarantees/' , views.contracts_guarantees  , name='contracts_guarantees'),
    path('<int:id>/project_meetings/' , views.project_meetings  , name='project_meetings'),
    path('<int:id>/project_Steps/' , views.project_Steps, name='project_Steps'),

]