from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
import datetime

from userservice.data.response.userresponse import  response_home_admission 
from userservice.data.request.userrequest import home_admission_request
from userservice.models import home_admission, person_details


# from userservice.utls.medicalutlls import utlis


class home_admission_service:
    
    def insert_home_admission(self, object):
        if object.get_id() is not None and object.get_id() != 0:
            # obj = home_admission  (goods_main model table name)
            obj = home_admission.objects.get(id=object.get_id())
            obj.person_details_id = object.get_person_details_id()
            obj.disease = object.get_disease()
            obj.if_new=object.get_if_new()
            obj.is_go_clinic=object.get_is_go_clinic()
            obj.room_no = object.get_room_no()
            obj.admission_date = object.get_admission_date()
            obj.given_things = object.get_given_things()
            obj.hospital_name = object.get_hospital_name()
            obj.bed_sores_status = object.get_bed_sores_status()
            obj.act_independently = object.get_act_independently()
            obj.toilet_managing = object.get_toilet_managing()
            obj.urine_managing = object.get_urine_managing()
            obj.work_in_uyirilai = object.get_work_in_uyirilai()
            obj.note = object.get_note()

            # Set discharge_reason and discharge_date only if provided
            if object.get_discharge_reason() is not None :
                obj.discharge_reason = object.get_discharge_reason()

            if object.get_discharge_date() is not None and object.get_discharge_date() != "None":
                obj.discharge_date = object.get_discharge_date()
                personObj = person_details.objects.filter(id=obj.person_details_id).update(person_type="Member")
                
            
            obj.save()
            
        else:
            # (obj = home_admission  (goods_main model table name))
            obj = home_admission(
                disease=object.get_disease(),
                person_details_id=object.get_person_details_id(),
                if_new=object.get_if_new(),
                room_no=object.get_room_no(),
                is_go_clinic=object.get_is_go_clinic(),
                admission_date=object.get_admission_date(),
                given_things=object.get_given_things(),
                hospital_name=object.get_hospital_name(),
                bed_sores_status=object.get_bed_sores_status(),
                act_independently=object.get_act_independently(),
                toilet_managing=object.get_toilet_managing(),
                urine_managing=object.get_urine_managing(),
                work_in_uyirilai=object.get_work_in_uyirilai(),
                note=object.get_note(),
                # discharge_reason=object.get_discharge_reason(),
                # discharge_date=object.get_discharge_date()  # Include discharge info if provided
            )
            obj.save()
            personObj = person_details.objects.filter(id=obj.person_details_id).update(person_type="Home Member")
            
        response = response_home_admission()
        response.set_id(obj.id)
        response.set_disease(obj.disease)
        response.set_if_new(str(obj.if_new))
        response.set_person_details_id(obj.person_details_id)
        response.set_admission_date(str(obj.admission_date))
        response.set_room_no(obj.room_no)
        response.set_given_things(obj.given_things)
        response.set_is_go_clinic(obj.is_go_clinic)
        response.set_hospital_name(obj.hospital_name)
        response.set_bed_sores_status(obj.bed_sores_status)
        response.set_act_independently(str(obj.act_independently))
        response.set_toilet_managing(obj.toilet_managing)
        response.set_urine_managing(obj.urine_managing)
        response.set_work_in_uyirilai(obj.work_in_uyirilai)
        # response.set_discharge_date(str(obj.discharge_date))
        # response.set_discharge_reason(obj.discharge_reason)
        response.set_note(obj.note)
        response.set_status(obj.status)

        return response

 
   
    
    
    #id used to get the details to the database
    def get_home_admission_details(self):
            
        condition = Q(status=1)
        obj_list = home_admission.objects.filter(condition)
        array_list = []
            
        for obj in obj_list:
            response = response_home_admission()
            response.set_id(obj.id)
            response.set_disease(obj.disease)
            response.set_if_new(str(obj.if_new))
            response.set_person_details_id(obj.person_details_id)
            response.set_admission_date(str(obj.admission_date))
            response.set_room_no(obj.room_no)
            response.set_given_things(obj.given_things)
            response.set_is_go_clinic(str(obj.is_go_clinic))
            response.set_hospital_name(obj.hospital_name)
            response.set_bed_sores_status(obj.bed_sores_status)
            response.set_act_independently(str(obj.act_independently))
            response.set_toilet_managing(obj.toilet_managing)
            response.set_urine_managing(obj.urine_managing)
            response.set_work_in_uyirilai(obj.work_in_uyirilai)
            response.set_discharge_date(str(obj.discharge_date))
            response.set_discharge_reason(obj.discharge_reason)
            response.set_note(obj.note)
            
            array_list.append(response.get())
        # print(array_list)
        return JsonResponse(array_list, safe=False)

        

    def delete_home_admission(self,id):
        obj=home_admission.objects.filter(id=id).update(status=0)
        response=response_home_admission()
        response.set_id("CATEGORY DELETED "+str(id))
        print("SUCCESSFULLY CATEGORY DELETED")
        return response
    
    
   