from django import template

register = template.Library()

@register.filter
def has_project_status(project_request):
    return project_request.projectstatus_set.exists()
