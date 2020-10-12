from django.shortcuts import render, redirect
from .models import Patients
from .forms import PatientsForm, UploadDocumentForm

from django.core.files.storage import FileSystemStorage

from .modules.doc_module import parse_doc_file
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def patients(request):
    patients = Patients.objects.all().order_by('-id')
    return render(request, 'main/patients.html', {'title':'Данные всех пациентов', 'patients': patients})


def upload_doc(request):
    form = UploadDocumentForm()
    return render(request, 'main/upload_doc.html', locals())


def add_patient(request):
    error = ''
    if request.method == 'POST':
        # если перешли от upload_doc
        if 'document' in request.FILES:
            myfile = request.FILES['document']
            data = parse_doc_file(myfile)
            form = PatientsForm(data)
            context = {'form': form}
            return render(request, 'main/add_patient.html', context)
        else:
            form = PatientsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('patients')
            else:
                error = 'Некорректные данные'
    # прямое открытие пустой формы (без перехода)
    form = PatientsForm()
    context = {'form': form}
    return render(request, 'main/add_patient.html', context)
