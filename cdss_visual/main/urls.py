from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('patients', views.patients, name='patients'),
    path('upload_doc', views.upload_doc, name='upload_doc'),
    path('add_patient', views.add_patient, name='add_patient'),
]
