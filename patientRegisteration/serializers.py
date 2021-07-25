from django.db.models import fields
from rest_framework import serializers
from .models import PatientRegister

class PatientRegisterSerializer(serializers.ModelSerializer):
  class Meta :
    fields=['id','name','age','disease','medicine','doctor_or_nurse','created_Date']
    model =PatientRegister