from django.contrib import admin
from django.urls import path
from .views import (
    HomepageTemplateView
)

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
