from django.shortcuts import render
from django.db import models
from rest_framework import generics, serializers
from .models import PatientRegister
from .serializers import PatientRegisterSerializer
# Create your views here.

class PatientRegisterListView(generics.ListCreateAPIView):
  serializer_class =PatientRegisterSerializer
  queryset =PatientRegister.objects.all()

class PatientRegisterDetailsView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class =PatientRegisterSerializer
  queryset =PatientRegister.objects.all()
