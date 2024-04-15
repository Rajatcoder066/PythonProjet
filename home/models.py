from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.CharField(max_length=122)
    message=models.CharField(max_length=1000)
    date=models.DateField()

    def __str__(self):
        return self.name
    
    
    
class Registration(models.Model):
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    password=models.CharField(max_length=1000)
    phone=models.CharField(max_length=1000)
    date=models.DateField()
    def __str__(self):
        return self.name

class Upload(models.Model):
    name=models.CharField(max_length=1000)
    url=models.CharField(max_length=10000)
    price=models.CharField(max_length=1000)
    offer=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    spec=models.CharField(max_length=1000)
    category=models.CharField(max_length=1000)
    date=models.DateField()
    def __str__(self):
        return self.name

