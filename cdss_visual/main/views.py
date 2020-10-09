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


def upload_doc(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)  # Do not forget to add: request.FILES
        if form.is_valid():
            #handle_uploaded_file(request.FILES['document'])
            # Do something with our files or simply save them
            # if saved, our files would be located in media/ folder under the project's base folder
            #form.save()

            myfile = request.FILES['document']
            #fs = FileSystemStorage()
            #filename = fs.save(myfile.name, myfile)
            #uploaded_file_url = fs.url(filename)

            data = parse_doc_file(myfile)
            request.session['info'] = data

            return redirect('add_patient')

        else:
            return redirect('about')
    return render(request, 'main/upload_doc.html', locals())


def add_patient(request):
    error = ''
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректные данные'

    old_post = request.session.get('info')

    form = PatientsForm(old_post)
    context = {'form': form}
    return render(request, 'main/create.html', context)
