from django.contrib import admin
from django.urls import path, include
from .views import (
    HomepageTemplateView,
    ContactFormView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
