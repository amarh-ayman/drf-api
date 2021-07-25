from django.urls import path

from .views import PatientRegisterListView, PatientRegisterDetailsView

urlpatterns = [
    path('', PatientRegisterListView.as_view(), name='patient_list'),

    path('<int:pk>', PatientRegisterDetailsView.as_view(), name='patient_detailes_api'), ]