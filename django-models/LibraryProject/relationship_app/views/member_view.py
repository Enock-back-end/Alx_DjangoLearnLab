from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
@login_required
def member_dashboard(request):
    return HttpResponse("Welcome to the Member Dashboard")
