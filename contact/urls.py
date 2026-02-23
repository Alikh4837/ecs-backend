from django.urls import path
from .views import ContactSubmissionCreate

urlpatterns = [
    path('contact/', ContactSubmissionCreate.as_view(), name='contact-submit'),
]