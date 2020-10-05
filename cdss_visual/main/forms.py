from .models import Patients
from django.forms import ModelForm, TextInput

class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО',
                }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО',
                }),
        }