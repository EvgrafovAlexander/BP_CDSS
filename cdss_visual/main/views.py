from django.shortcuts import render, redirect
from .models import Patients
from .forms import PatientsForm

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def patients(request):
    patients = Patients.objects.all()
    return render(request, 'main/patients.html', {'title':'Данные всех пациентов', 'patients':patients})

def create(request):
    error = ''
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректные данные'

    form = PatientsForm()
    context = {'form': form}
    return render(request, 'main/create.html', context)