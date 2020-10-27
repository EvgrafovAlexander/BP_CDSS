from .models import Patients, Document, CompleteBloodCount
from django.forms import ModelForm, TextInput, FileInput, DateInput, Textarea


class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ["first_name", "last_name", "middle_name",
                  "date_of_birth", "receipt_date", "discharge_date",
                  "base_diag", "complication_diag", "accompanying_diag"]
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
            "date_of_birth": DateInput(format=('%d.%m.%Y'),
                                       attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Введите дату рождения',
                                            'type': 'text'
                                        }),
            "receipt_date": DateInput(format=('%d.%m.%Y'),
                                      attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Введите дату поступления в стационар',
                                            'type': 'text'
                                        }),
            "discharge_date": DateInput(format=('%d.%m.%Y'),
                                        attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Введите дату выписки из стационара',
                                             'type': 'text'
                                        }),
            "base_diag": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация об основном диагнозе',
                'rows': 5,
                'cols': 30,
            }),
            "complication_diag": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация об осложнениях',
                'rows': 5,
                'cols': 30,
            }),
            "accompanying_diag": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о сопутствующих заболеваниях',
                'rows': 5,
                'cols': 30,
            }),

        }


class CompleteBloodCountForm(ModelForm):
    class Meta:
        model = CompleteBloodCount
        fields = ["date_cbc", ]
        widgets = {
            "date_cbc": DateInput(format=('%d.%m.%Y'),
                                       attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Введите дату анализа',
                                            'type': 'text'
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
