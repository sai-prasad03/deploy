
from django.shortcuts import render,redirect
from .models import Applicant
from django.http import HttpResponse

# Create your views here.

def vaccancy(request):
    if request.method == 'GET':
        return render(request,'app/home.html')

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        job_role = request.POST["job_role"]
        address = request.POST["address"]
        city = request.POST["city"]
        pincode = request.POST["pincode"]
        date= request.POST["pincode"]
        file  = request.POST["file"]

        entry = Applicant(first_name=first_name,last_name=last_name,email=email,
        job_role=job_role,
        address=address,city=city, pincode=pincode,date=date,
        file=file)

        entry.save()
        return HttpResponse("Your job Application submitted Successfull..!!")
