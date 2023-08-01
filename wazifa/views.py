from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.




def job_list(request):
    job_list = Job.objects.all() #get all jobs
    # paginator setup
    paginator = Paginator(job_list, 8)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'wazifa/job_list.html', {'jobs':page_obj}) #--> template name


def job_detail(request, slug):
   job_detail = Job.objects.get(slug=slug) #get 1 job
   return render(request, 'wazifa/job_detail.html', {'job':job_detail}) #--> template name


