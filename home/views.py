from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random
from home.models import studentdetail,Customuser
from home.forms import CustomuserForms
from home.forms import StudentProfileForm


def func_one(request):
    value='Django App'
    
    return HttpResponse(value)

def home(request):
    value = 'Welcome To Home Page'
    return HttpResponse(value)

def remark(request):
    feed = ('Tremendous Job','Excellent Work','Not Satisfied','Do it again','Perfect','Well done',)
    
    item = random.choice(feed) 
    return HttpResponse(item)


       
def user(request, **kwargs):
    print(kwargs['name'])
    print(kwargs['registration_number'])
    print(kwargs['branch'])
    print(kwargs['yearsofstudy'])
    print(kwargs['mobile_number'])
    print(kwargs['email'])
    print(kwargs['gender'])
    print(kwargs['current_address'])
    print(kwargs['permanent_address'])
    print(kwargs['nationality'])
    
  
    studentdetail.objects.create(
        name = kwargs['name'],
        registration_number = kwargs['registration_number'],
        branch = kwargs['branch'],
        yearsofstudy = kwargs['yearsofstudy'],
        mobile_number = kwargs['mobile_number'],
        email = kwargs['email'],
        gender = kwargs['gender'],
        current_address = kwargs['current_address'],
        permanent_address = kwargs['permanent_address'],
        nationality = kwargs['nationality'],
        
    ) 
    
    detail = studentdetail.objects.all()
    
    if len(detail) > 4:
        studentdetail.objects.all().delete()
    return HttpResponse(detail)



def homepage(request):
    
   if request.method == 'POST':
       print(request.POST)
    
       studentdetail.objects.create(
           name= request.POST['name'],
           registration_number= request.POST['registrationnumber'],
           branch= request.POST['branch'],
           yearsofstudy = request.POST['yearsofstudy'],
           mobile_number = request.POST['mobilenumber'],
           email = request.POST['email'],
           gender = request.POST['gender'],
           current_address = request.POST['currentaddress'],
           permanent_address = request.POST['permanentaddress'],
           nationality  = request.POST['nationality'],                 
        )
      
       students= studentdetail.objects.all()
        
        
       if len(students) > 4:
           studentdetail.objects.all().delete()
    
    
       context = {
        'students': students
    }
    
       return render(request,'about.html',context)






       
       
       
   return render(request,'homepage.html') 


def showform(request):
    #create an instance of the form
    form = CustomuserForms()
 
    #check if the request method is POST
    if request.method == 'POST':

        #print all the data
        print(request.POST)

        #save all the data above in the database
   
        student = Customuser.objects.create(
           name= request.POST['Name'],
           registration_number= request.POST['Registration_number'],
           branch= request.POST['Branch'],
           yearsofstudy = request.POST['Yearsofstudy'],
           mobile_number = request.POST['Mobile_number'],
           email = request.POST['Email'],
           gender = request.POST['Gender'],
           current_address = request.POST['Current_address'],
           permanent_address = request.POST['Permanent_address'],
           nationality  = request.POST['Nationality'],  )
         
        students = Customuser.objects.all()


    context = { 'forms': form, }

    return render(request, 'formpage.html', context)  


#create a brand new page
def modelformview(request):

    #check if the request method is POST
    if request.method == 'POST':

        #create an instance of the form
        form = StudentProfileForm(request.POST)
        print(form.errors)

        # checking the form is valid or not
        if form.is_valid():
            
            form.save()
        # if the form is not valid then print False    
        else:
            print(False)
        #pass the form in the context for use in the HTML Template
        context = {
            'form': form,
            'errors':form.errors
        }            
        return render(request, 'studentform.html', context)

    
    form = StudentProfileForm()

    #pass the form in the context for use in the HTML Template
    context = {
        'form': form,
    }
    return render(request,'studentform.html',context )   