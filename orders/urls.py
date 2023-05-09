from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('request_order_for_company/' , views.request_order_for_company  , name='request_order_for_company'),
]