from django.contrib import admin

from .models import ConsultationRequest , ProjectRequest ,ConsultationComment
admin.site.register(ConsultationRequest)
admin.site.register(ProjectRequest)
admin.site.register(ConsultationComment)