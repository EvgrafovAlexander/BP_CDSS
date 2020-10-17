from .models import Patients, Document
from django.forms import ModelForm, TextInput, FileInput, DateInput


class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ["first_name", "last_name", "middle_name", "date_of_birth"]
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
                }),
            "middle_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество',
            }),
            "date_of_birth": DateInput(format=('%d-%m-%Y'),
                 attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения',
                'type': 'date'
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
