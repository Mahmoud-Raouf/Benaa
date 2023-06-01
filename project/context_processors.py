
from accounts.models import Profile


def profile_fields(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return {'profile_fields': profile}
    return{}
