from django.db import models
from accounts.models import CustomeUser


class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
class Researchlab(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.title
    

    
    
class Doctor(models.Model):
    image= models.ImageField(upload_to='doctor',default='doctor.png')
    info = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    twitter= models.CharField(max_length=200,default='#')
    facebook= models.CharField(max_length=200,default='#')
    instagram= models.CharField(max_length=200,default='#')
    linkdin= models.CharField(max_length=200,default='#')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username
    
class Departments(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='department',default='department.jpg')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery',default='gallery.jpg')


class Testimonials(models.Model):
    info = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='testimonial',default='people.jpg')
    skills = models.ManyToManyField(Skills)
    description = models.TextField()

    def __str__(self):
        return self.info.username
    
class Price(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    content5 = models.TextField()

    def __str__(self):
        return self.title
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    appointment_date = models.DateTimeField()
    select_department = models.ManyToManyField(Departments)
    select_doctor = models.ManyToManyField(Doctor)
    message = models.TextField()

    def __str__(self):
        return self.name
    



class NewsLetter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    