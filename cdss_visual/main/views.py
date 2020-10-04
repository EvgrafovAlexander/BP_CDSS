from django.shortcuts import render
from .models import TableFirst

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def patients(request):
    patients = TableFirst.objects.all()
    return render(request, 'main/patients.html', {'title':'Данные всех пациентов', 'patients':patients})