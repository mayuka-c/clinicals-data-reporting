from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicalsApp.models import Patient, ClinicalData
from clinicalsApp.forms import ClinicalDataForms

# Create your views here.

class PatientListView(ListView):
    model = Patient
    # default template - patient_list.html

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')
    # default template - patient_form.html

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')
    # default template - patient_form.html

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    # default template - patient_confirm_delete.html

def addClinicalData(request, **kwargs):
    form = ClinicalDataForms()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == "POST":
        form = ClinicalDataForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {'form': form, 'patient': patient})

def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            # height - feet, weight - kg
            heightWeight = eachEntry.componentValue.split('/')
            if len(heightWeight) > 1:
                feetToMeters = float(heightWeight[0]) * 0.4536
                BMI = (float(heightWeight[1]))/(feetToMeters * feetToMeters)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                # bmiEntry.save()
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request, 'clinicalsApp/generateReport.html',{'data':responseData})