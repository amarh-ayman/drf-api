from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.

class PatientRegister(models.Model):
  name = models.CharField(max_length=64)
  age = models.IntegerField()
  idNum=models.IntegerField(default=0)
  disease =models.TextField()
  medicine=models.TextField()
  doctor_or_nurse =models.ForeignKey(get_user_model(),on_delete=CASCADE)
  created_Date=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
