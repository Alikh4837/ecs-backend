from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

class ContactSubmissionCreate(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer