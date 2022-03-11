from django.views import generic
from .models import *
from .forms import ContactForm
from django.contrib import messages


class HomepageTemplateView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['form'] = ContactForm()
        context['testimonials'] = Testimonial.objects.all()
        context['socialmedias'] = SocialMedia.objects.all()
        context['educations'] = Education.objects.order_by('ordering')
        context['employments'] = Employment.objects.order_by('ordering')
        context['projects'] = Project.objects.all()
        context['categories'] = ProjectCategory.objects.all()
        return context


class ContactFormView(generic.FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        print('thank you for submitting the form mate!!!')
        form.save()
        messages.success(self.request, 'Query has been sent already! Send another if needed.')
        return super().form_valid(form)
