from django.contrib import admin
from django.urls import path
from home import views
from home.views import func_one,remark,user,home,showform,modelformview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form', showform, name='form'),
    path('studentform', modelformview, name='form'),
    path('', home,),
    path('home', func_one, name='home'),
    path('feed', remark, name= 'remark'),
    path('student/<str:name>/<int:registration_number>/<str:branch>/<int:yearsofstudy>/<int:mobile_number>/<str:email>/<str:gender>/<str:current_address>/<str:permanent_address>/<str:nationality>/',user),
    path('start', views.homepage,name="homepage"),
    
]
