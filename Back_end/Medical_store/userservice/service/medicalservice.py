from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
import datetime

from userservice.data.response.userresponse import  response_home_admission ,dropdown_response
from userservice.data.request.userrequest import home_admission_request
from userservice.models import home_admission, dropdown_table


# from userservice.utls.medicalutlls import utlis


class home_admission_service:
    
    def insert_home_admission(self, object):
        print(object)
        if object.get_id() is not None and object.get_id() != 0:
              # obj = home_admission  (goods_main model table name)
            obj1 = home_admission.objects.filter(id=object.get_id()).update(
                disease=object.get_disease(),                                                          
                person_details_id=object.get_person_details(),
                room_no=object.get_room_no(),
                given_things=object.get_given_things(),
                hospital_name=object.get_hospital_name(),
                bed_source_image=object.get_bed_source_image(),
                able_to_act_independently=object.get_able_to_act_independently(),
                toilet_managing=object.get_toilet_managing(),
                urine_managing=object.get_urine_managing(),
                work_in_uyirilai=object.get_work_in_uyirilai(),
                discharge_date=object.get_discharge_date(),            
                discharge_reason=object.get_discharge_reason(),
                note=object.get_note())
            
            obj=home_admission.objects.get(id=object.get_id())
            
        else:
            # (obj = home_admission  (goods_main model table name))
            obj = home_admission(
            disease =object.get_disease(),
            person_details_id=object.get_person_details(),
            room_no=object.get_room_no(),
            admission_date=object.get_admission_date(),  
            given_things=object.get_given_things(),
            hospital_name=object.get_hospital_name(),
            bed_source_image=object.get_bed_source_image(),
            able_to_act_independently=object.get_able_to_act_independently(),
            toilet_managing=object.get_toilet_managing(),
            urine_managing=object.get_urine_managing(),
            work_in_uyirilai=object.get_work_in_uyirilai(),
            discharge_date=object.get_discharge_date(),            
            discharge_reason=object.get_discharge_reason(),
            note=object.get_note())
            obj.save()

        response = response_home_admission()
        response.set_id(obj.id)
        response.set_disease(obj.disease)
        response.set_if_new(obj.if_new)
        response.set_person_details(obj.person_details_id)
        response.set_admission_date(str(obj.admission_date))
        response.set_room_no(obj.room_no)
        response.set_given_things(obj.given_things)
        response.set_is_go_clinic(obj.is_go_clinic)
        response.set_hospital_name(obj.hospital_name)
        response.set_bed_source_image(obj.bed_source_image)
        response.set_able_to_act_independently(obj.able_to_act_independently)
        response.set_toilet_managing(obj.toilet_managing)
        response.set_urine_managing(obj.urine_managing)
        response.set_work_in_uyirilai(obj.work_in_uyirilai)
        date=obj.discharge_date
        response.set_discharge_date(str(date))
        response.set_discharge_reason(obj.discharge_reason)
        response.set_note(obj.note)
        response.set_status(obj.status)

        return response


 
 
    def drop_down(self, key,query):
        condition = Q(status=1)
        if key != "" and key != None:
            condition &= Q(list_type=key)  # key are list types example districts , items , address can we dicite any name
            
        if query != "" and query != None:
            condition &= Q(list_value__icontains=query)
        dropdown_list = dropdown_table.objects.filter(condition)
        print(dropdown_list.query)
        array=[]
        for obj in dropdown_list:
            response = dropdown_response()
            response.set_id(obj.id)
            response.set_list_type(obj.list_type)
            response.set_list_value(obj.list_value)
            response.set_status(obj.status)
            array.append(response.get())

        return array
    
    
    
    #id used to get the details to the database
    def get_home_admission_details(self):
            
        condition = Q(status=1)
        obj_list = home_admission.objects.filter(condition)
        array_list = []
            
        for obj in obj_list:
            response = response_home_admission()
            response.set_id(obj.id)
            response.set_disease(obj.disease)
            response.set_if_new(obj.if_new)
            response.set_person_details(obj.person_details_id)
            response.set_admission_date(str(obj.admission_date))
            response.set_room_no(obj.room_no)
            response.set_given_things(obj.given_things)
            response.set_is_go_clinic(obj.is_go_clinic)
            response.set_hospital_name(obj.hospital_name)
            response.set_bed_source_image(obj.bed_source_image)
            response.set_able_to_act_independently(obj.able_to_act_independently)
            response.set_toilet_managing(obj.toilet_managing)
            response.set_urine_managing(obj.urine_managing)
            response.set_work_in_uyirilai(obj.work_in_uyirilai)
            date=obj.discharge_date
            response.set_discharge_date(str(date))
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