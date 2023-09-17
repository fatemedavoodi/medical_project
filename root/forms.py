from django import forms
from .models import NewsLetter,ContactUs,Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['name','email','phone','appointment_date','select_department','select_doctor','message']

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ['name','email','subject','message']



class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = ['email']



