from django.urls import path
from . import views
from userservice.controller import usercontroller

urlpatterns=[
    path('home_admission_insert',usercontroller.insert_homeadmission),
    path('drop_down_',usercontroller.drop_down),
    path('delete',usercontroller.retrify_home_admission),
    
   
]