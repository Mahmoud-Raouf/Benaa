from django import forms
from .models import ConsultationRequest , ConsultationComment, Contracts_Guarantees, ProjectMeetings, ProjectRequest, ProjectStatus




class RequestForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ("name" ,"description")
        
        
        
class ProjectRequestForm(forms.ModelForm):
    class Meta:
        model = ProjectRequest
        fields = ("workname" ,"name" , "workType" ,"city" ,"description" )


class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = ProjectStatus
        fields = ("request_status", "image_status" ,"description" ,  )
        
        
class Contracts_GuaranteesForm(forms.ModelForm):
    class Meta:
        model = Contracts_Guarantees
        fields = ("image_status" ,"materials_used" , "description" )


class ProjectMeetingsForm(forms.ModelForm):
    class Meta:
        model = ProjectMeetings
        
        fields = ("name" , "description" )


class CommentForm(forms.ModelForm):

    class Meta:
        model = ConsultationComment
        fields = ('text',)