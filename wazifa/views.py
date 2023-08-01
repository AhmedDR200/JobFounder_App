from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm
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

    # apply form
   if request.method =='POST':
       form =ApplyForm(request.POST, request.FILES) #بنتعامل مع فايلز
       if form.is_valid():
           myform = form.save(commit=False) #عشان ميبقاش في ايرور لاني مش حاطط الوظيفة ف الفيلدز 
           myform.job = job_detail
           myform.save()
   else:
         form = ApplyForm()
      
   return render(request, 'wazifa/job_detail.html', {'job':job_detail , 'form':form}) #--> template name


