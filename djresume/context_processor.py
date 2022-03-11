from django.contrib.auth.models import User
from .forms import ContactForm
from .models import SocialMedia


def project_context(request):
    context = {
        'title': 'Digital Resume',
        'me': User.objects.first(),
        'form': ContactForm(),
        'socialmedias': SocialMedia.objects.all()
    }
    return context
