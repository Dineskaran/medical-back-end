from django.urls import path
from . import views
from userservice.controller import usercontroller,nursedutycontroller,userdetailscontroller,dropdowncontroller
from userservice.controller import personcontroller
from userservice.controller import logininfocontroller


urlpatterns=[
    path('home_admission_insert',usercontroller.insert_homeadmission),
    path('delete',usercontroller.retrify_home_admission),
    
    path('insert_drop_down',dropdowncontroller.insert_dropdown),
    path('drop_down_distin',dropdowncontroller.drop_down_distin),
    path('delete_dropdown',dropdowncontroller.delete_drop_down),
    
    path('insert_nurse_duty',nursedutycontroller.insert_nurse_duty_details),
    path('delete_nurse_duty_details',nursedutycontroller.delete_nurse_duty_details,name="delete_nurse_duty_details"),
    path('count_duty_option',nursedutycontroller.duty_option_count_details),
    path('nurse_duty_report',nursedutycontroller.nurse_duty_report_details, name='nurse_duty_report'),
    
    path('insert_prson_details',personcontroller.insert_prson_details,name="insert_prson_details"),
    path('delete_prson_details',personcontroller.delete_person_details,name="delete_person_details"),
    
    path('insert_user_details',userdetailscontroller.insert_user,name="insert_user_details"),
    path('manage_user_details',userdetailscontroller.manage_user,name="delete_user_details"),
    path('change password',userdetailscontroller.change_password),
    path('login',userdetailscontroller.login),
     path('blockuser',userdetailscontroller.block_user, name='block_user'),
    
    path('insert_log_details',logininfocontroller.insert_log,name="insert_log_details"),
    path('delete_log_details',logininfocontroller.delete_log_details,name="delete_log_details"),
   
]