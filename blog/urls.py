from django.urls import path
from .views import BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>', BlogDetailView.as_view(), name='blog-details')
]
