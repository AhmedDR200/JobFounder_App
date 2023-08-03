from django.shortcuts import render , redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm , JobForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.




def job_list(request):
    job_list = Job.objects.all() #get all jobs

        # filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list =myfilter.qs

    # paginator setup
    paginator = Paginator(job_list, 8)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'wazifa/job_list.html', {'jobs':page_obj , 'myfilter':myfilter}) #--> template name




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




@login_required
def add_job(request):
    if request.method =='POST':
        form =JobForm(request.POST, files=request.FILES )
        if form.is_valid():
            myform = form.save(commit=False)# save the data to database
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list')) #بيرجعني على ليست الوظايف بعد ما ب بوست الوظيفة
    else:
        form = JobForm()
    return render(request, 'wazifa/add_job.html', {'form':form})
    


