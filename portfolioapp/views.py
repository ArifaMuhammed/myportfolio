from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def resume(request):
    return render(request,'resume.html')
def project(request):
    return render(request,'projects.html')
def contact(request):
 if request.method=="POST":
    contact=Contact()
    name=request.POST.get('name')
    email=request.POST.get('email')
    Phone =request.POST.get('phone')
    description=request.POST.get('description')
    contact.name=name
    contact.email=email
    contact.phonenumber=Phone
    contact.description=description
    contact.save()
    return HttpResponse("<h1>THANK FOR CONTACT US</h1>")
 return render(request,'contact.html')
