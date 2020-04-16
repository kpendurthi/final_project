from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Employer, Job
from .forms import EmployerForm, JobForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def employer_list(request):
    employers = Employer.objects.all()
    return render(request, 'jobsapp/employer_list.html', {'employers': employers})

@login_required
def employer_detail(request, pk):
    employer = Employer.objects.get(id=pk)
    return render(request, 'jobsapp/employer_detail.html', {'employer': employer})

@login_required
def employer_create(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            employer = form.save()
            return redirect('employer_detail', pk=employer.pk)
    else:
        form = EmployerForm()
    return render(request, 'jobsapp/employer_form.html', {'form': form})

@login_required
def employer_edit(request, pk):
    employer = Employer.objects.get(pk=pk)
    if request.method == "POST":
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            employer = form.save()
            return redirect('employer_detail', pk=employer.pk)
    else:
        form = EmployerForm(instance=employer)
    return render(request, 'jobsapp/employer_form.html', {'form': form})

@login_required
def employer_delete(request, pk):
    Employer.objects.get(id=pk).delete()
    return redirect('employer_list')

# def jobs_list(request):
#     jobs = Job.objects.all()
#     return render(request, 'jobsapp/job_list.html', {'jobs': jobs})

# def jobsearch_list(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#            jobs = Job.objects.filter(location__contains=form.cleaned_data['location'],title__contains=form.cleaned_data['position'])
#            return render(request, 'jobsapp/job_list.html', {'jobs': jobs})
#     else:
#         form = SearchForm()
#     return render(request, 'jobsapp/jobsearch_form.html', {'form': form})

class HomeView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'
    
    def get_queryset(self):
        return self.model.objects.all()[:5]

class SearchView(ListView):
    model = Job
    template_name = 'search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['position'])

class JobListView(ListView):
    model = Job
    template_name = 'jobsapp/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 5

@login_required
def job_detail(request, pk):
    job = Job.objects.get(id=pk)
    return render(request, 'jobsapp/job_detail.html', {'job': job})

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'jobsapp/job_form.html', {'form': form})

@login_required
def job_edit(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save()
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'jobsapp/job_form.html', {'form': form})

@login_required  
def job_delete(request, pk):
    Job.objects.get(id=pk).delete()
    return redirect('job_list') 



    