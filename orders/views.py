from django.shortcuts import render

from request.models import ConsultationRequest


def request_order_for_company(request):
    request_order_for_company  = ConsultationRequest.objects.filter(user = request.user)

    return render(request ,'request_order_for_company.html', {
        'request_order_for_company' : request_order_for_company ,
        'title' : 'طلبات إستشارة العملاء',

    })