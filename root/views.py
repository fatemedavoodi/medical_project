from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
    if request.method == 'GET':
        service = Service.objects.filter(status=True)
        researchlab = Researchlab.objects.all()
        department = Departments.objects.filter(status=True)
        testimonial = Testimonials.objects.all()
        doctor = Doctor.objects.filter(status=True)
        gallery = Gallery.objects.all()
        price = Price.objects.all()
        doctor_count = Doctor.objects.filter(status=True).count()
        department_count = Departments.objects.filter(status=True).count()
        researchlab_count = Researchlab.objects.filter(status=True).count()
        service_count = Service.objects.filter(status=True).count()

        context={
            'service': service,
            'researchlab': researchlab,
            'department': department,
            'testimonial': testimonial,
            'doctor': doctor,
            'gallery': gallery,
            'price': price,
            'drc': doctor_count,
            'dc': department_count,
            'rc': researchlab_count,
            'sc': service_count,
        }
        return render(request,'root/index.html',context=context)
    elif request.method == 'POST' and len(request.POST)==2:
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect(request.path_info)   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect(request.path_info)
        
    elif request.method == 'POST' and len(request.POST)==5:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'we recieved your message we call you as soon')
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:home')
        
    elif request.method == 'POST' and len(request.POST)>5:
        form = Appointment(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'we recieved your message we call you as soon')
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:home')

