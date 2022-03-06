from django.contrib.auth.models import User


def project_context(request):
    context = {
        'title': 'Digital Resume',
        'me': User.objects.first()
    }
    return context
