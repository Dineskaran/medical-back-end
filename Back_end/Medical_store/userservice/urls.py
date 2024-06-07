from django.urls import path
from . import views
from userservice.controller import usercontroller,nursedutycontroller

urlpatterns=[
    path('home_admission_insert',usercontroller.insert_homeadmission),
    path('drop_down_',usercontroller.drop_down),
    path('delete',usercontroller.retrify_home_admission),
    path('insert_nurse_duty',nursedutycontroller.insert_nurse_duty_details),
    path('delete_nurse_duty_details',nursedutycontroller.delete_nurse_duty_details,name="delete_nurse_duty_details"),
   
]