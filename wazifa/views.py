from django.shortcuts import render
from .models import Job
# Create your views here.




def job_list(request):
    job_list = Job.objects.all() #get all jobs
    return render(request, 'wazifa/job_list.html', {'jobs':job_list}) #--> template name


def job_detail(request, id):
   job_detail = Job.objects.get(id=id) #get 1 job
   return render(request, 'wazifa/job_detail.html', {'job':job_detail}) #--> template name


