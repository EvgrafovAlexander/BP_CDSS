from .models import Patients, Document
from django.forms import ModelForm, TextInput, FileInput

class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
                }),
        }


class UploadDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ["document"]
        widgets = {
            "document": FileInput(attrs={
                'class': 'form-data',
            })}


class AddPatientForm(ModelForm):
    class Meta:
        model = Patients
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'value': Patients.first_name,
                }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'value': Patients.last_name,
                }),
        }