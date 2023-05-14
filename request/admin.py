from django.contrib import admin

from .models import *
admin.site.register(ConsultationRequest)
admin.site.register(ProjectRequest)
admin.site.register(ConsultationComment)
admin.site.register(ProjectStatus)
admin.site.register(Contracts_Guarantees)
admin.site.register(ProjectMeetings)