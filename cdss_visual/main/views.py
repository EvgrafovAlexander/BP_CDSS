from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Patients
from .forms import PatientsForm, UploadDocumentForm

from django.views.generic import DetailView, UpdateView, DeleteView, \
                                 TemplateView, ListView

from .modules.doc_module import parse_doc_file
# Create your views here.


class SearchView(TemplateView):
    template_name = 'search.html'


class SearchResultsView(ListView):
    model = Patients
    template_name = 'search_results.html'
    context_object_name = 'patient'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Patients.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return object_list


class PatientDetailView(DetailView):
    model = Patients
    template_name = 'main/details_view.html'
    context_object_name = 'patient'


class PatientUpdateView(UpdateView):
    model = Patients
    template_name = 'main/add_patient.html'
    form_class = PatientsForm


class PatientDeleteView(DeleteView):
    model = Patients
    template_name = 'main/del_patient.html'
    success_url = '/patients'


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def patients(request):
    patients = Patients.objects.all().order_by('-id')
    return render(request, 'main/patients.html', {'title': 'Данные всех пациентов', 'patients': patients})


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
            patients_form = PatientsForm(data['text_data'])
            context = {'patients_form': patients_form}
            return render(request, 'main/add_patient.html', context)
        else:
            patients_form = PatientsForm(request.POST)
            if patients_form.is_valid():
                patients_form.save()
                return redirect('patients')
            else:
                error = 'Некорректные данные'
    # прямое открытие пустой формы (без перехода)
    patients_form = PatientsForm()
    context = {'patients_form': patients_form}
    return render(request, 'main/add_patient.html', context)


def del_patient(request):
    return render(request, 'main/del_patient.html')
