from django.db import models

class studentdetail(models.Model):
    
    name = models.CharField(max_length=200)
    registration_number = models.IntegerField(default=30)
    branch = models.CharField(max_length=30)
    yearsofstudy = models.IntegerField(default= 10)
    mobile_number = models.IntegerField(default=200)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    current_address = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    
    
    
    
    
   
   
    def __str__(self):
        return self.name


class Customuser(models.Model):
    name = models.CharField(max_length=200)
    registration_number = models.IntegerField(default=30)
    branch = models.CharField(max_length=30)
    yearsofstudy = models.IntegerField(default= 10)
    mobile_number = models.IntegerField(default=200)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    current_address = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
      

      
    def __str__(self):
        return self.name




class StudentProfile(models.Model):
    name = models.CharField(max_length=200)
    registration_number = models.IntegerField() 
    branch = models.CharField(max_length=30)
    yearsofstudy = models.IntegerField()
    mobile_number = models.IntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)  


     
    def __str__(self):
        return self.name   








