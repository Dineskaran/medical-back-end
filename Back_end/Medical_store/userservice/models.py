from django.db import models
import datetime
from django.utils.timezone import now




# 01. goods_main  table model

class goods_main(models.Model):
    goods_type=models.CharField(max_length=75,null=True)
    item_name=models.CharField(max_length=255,null=True)
    item_brand=models.CharField(max_length=100,null=True)
    item_description=models.CharField(max_length=255,null=True)
    quantity=models.FloatField(null=True)
    unit=models.CharField(max_length=20,null=True)
    num_of_exp_date=models.IntegerField(null=True)
    status=models.IntegerField(default=1)
    
    class Meta:
        db_table='goods_main'



# 02. supplier  table model

class supplier(models.Model):
    supplier_type=models.CharField(max_length=150,null=True)
    supplier_name=models.CharField(max_length=255 ,null=False)
    supplier_address=models.CharField(max_length=255,null=True)
    contry=models.CharField(max_length=75,null=True)
    contact_number=models.CharField(max_length=15,null=True)
    status=models.IntegerField(default=1)
    
    class Meta:
        db_table='supplier'
        

        

# 03. in details  table model

class in_details(models.Model):
    goods_main=models.ForeignKey("goods_main",on_delete=models.CASCADE, null=True)
    in_quantity=models.FloatField(null=True)
    unit=models.CharField(max_length=20,null=True)
    in_date=models.DateField(null=True)
    exp_date=models.DateField(null=True)
    in_type=models.CharField(max_length=120 ,null=True)
    available_stock=models.FloatField(null=True)
    supplier=models.ForeignKey("supplier",on_delete=models.CASCADE, null=True)
    status=models.IntegerField(default=1)
    
    
    class Meta:
        db_table='in_details'



# 04. out Details  table model


class out_details(models.Model):
    in_details=models.ForeignKey("in_details",on_delete=models.CASCADE, null=True)
    out_date=models.DateField(null=True)
    out_type=models.CharField(max_length=120,null=True)
    out_quantity=models.FloatField(null=True)
    out_unit=models.CharField(max_length=20,null=True)
    person_details=models.ForeignKey("person_details",on_delete=models.CASCADE, null=True)
    by_whom=models.CharField(max_length=120,null=True)
    status=models.IntegerField(default=1)
    
    class Meta:
        db_table='out_details'
        


# 05. person table model        

class person_details(models.Model):
    person_type=models.CharField(max_length=45,null=True)
    person_no=models.CharField(max_length=15,null=True)
    first_name=models.CharField(max_length=75,null=True)
    last_name=models.CharField(max_length=75,null=True)
    date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=20,null=True)
    civil_status=models.CharField(max_length=30,null=True)
    nic=models.CharField(max_length=15,null=True)
    effect=models.CharField(max_length=45,null=True)
    effect_type=models.CharField(max_length=45,null=True)
    effect_status=models.CharField(max_length=45,null=True)
    effect_reason=models.CharField(max_length=45,null=True)
    effect_date=models.DateField(null=True)
    is_bed_sore=models.BinaryField(null=True)  # only 0,1 used then 1=yes,0=no
    contact_number=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=255,null=True)
    district=models.CharField(max_length=60,null=True)
    now_status=models.CharField(max_length=45,null=True)
    status=models.IntegerField(default=1)
    
    
    class Meta:
        db_table="person_details"
        


# 06. HomeAdmission  table  model

class home_admission(models.Model):  
    person_details=models.ForeignKey("person_details",on_delete=models.CASCADE)
    if_new=models.SmallIntegerField(default=0,null=True) # defauld 0 means New 1 old person
    disease=models.CharField(max_length=75,null=True)
    admission_date=models.DateField(null=True)
    room_no=models.CharField(max_length=15,null=True)
    given_things=models.CharField(max_length=120,null=True)
    is_go_clinic=models.SmallIntegerField(default=0,null=True)
    hospital_name=models.CharField(max_length=255,null=True)
    bed_source_image=models.CharField(max_length=200,null=True)
    able_to_act_independently=models.SmallIntegerField(default=0,null=True)
    toilet_managing=models.CharField(max_length=255,null=True)
    urine_managing=models.CharField(max_length=255,null=True)
    work_in_uyirilai=models.CharField(max_length=75,null=True)
    discharge_date=models.DateField(null=True)
    discharge_reason=models.CharField(max_length=120,null=True)
    note=models.CharField(max_length=150,null=True)
    status=models.IntegerField(default=1)
    
    class Meta:
        db_table="home_admission"
    


# 07. NurseDuty table model

class nurse_duty(models.Model):
    date=models.DateTimeField(null=True)
    time=models.TimeField(null=True)
    person_details=models.ForeignKey("person_details", on_delete=models.CASCADE)
    person_type=models.CharField(max_length=45,null=True)
    duty_option=models.CharField(max_length=120,null=True)
    status=models.IntegerField(default=1)
    note=models.CharField(max_length=150,null=True)
    
    class Meta:
        db_table="nurse_duty"



# 08. User Details table model

class user_details(models.Model):
    user_name=models.CharField(max_length=30,null=True)
    user_id=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=255,null=True)
    privilege=models.CharField(max_length=120,null=True)
    create_date=models.DateField(default=now)
    create_by=models.CharField(max_length=15,null=True)
    status=models.IntegerField(default=1)
    
    class Meta:
        db_table="user_details"



# 09. login info table model

class login_info(models.Model):

    user_details=models.ForeignKey("user_details",on_delete=models.CASCADE)
    log_date=models.DateTimeField(default=now)
    log_time=models.TimeField(null=True)
    location=models.CharField(max_length=255)
    log_out_time=models.TimeField(null=True)
    num_of_attempt=models.TimeField(null=True) 
    log_status=models.IntegerField(null=True)
    status=models.IntegerField(default=1)
    
    class Meta:
        db_table = "login_info"



# 10. drop down  table model

class dropdown_table(models.Model):
    list_type=models.CharField(max_length=60,null=True)
    list_value=models.CharField(max_length=255,null=True)
    filter_by = models.CharField(max_length=60, null=True)
    status=models.IntegerField(default=1)
    
    
    class Meta:
        db_table="dropdown_table"
      