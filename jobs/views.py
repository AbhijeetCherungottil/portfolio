import jobs
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Job
# Create your views here.
def index(request):
    jobs = Job.objects
    return render(request,'jobs/index.html',{'jobs':jobs})
def detail(request,job_id):
    jobs_detail=get_object_or_404(Job,pk=job_id)
    print(jobs_detail)
    return render(request,'jobs/details.html',{'jobs':jobs_detail})    