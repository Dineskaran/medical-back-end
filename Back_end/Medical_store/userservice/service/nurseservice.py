from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
import datetime
from django.db.models import Count


from userservice.data.response.nurseresponse import nurse_duty_response,dutyCountResponse
from userservice.data.request.nurserequest import nurse_duty_request
from userservice.models import nurse_duty

class nurse_duty_service:
    
    def insert_nurse_duty(self, object):
        if object.get_id() is not None and object.get_id() != 0:
            # Update existing nurse duty record
            obj1=nurse_duty.objects.filter(id=object.get_id()).update(
                date=object.get_date(),
                time=object.get_time(),
                person_details_id=object.get_person_details_id(),
                person_type=object.get_person_type(),
                duty_option=object.get_duty_option(),
                note=object.get_note(),
                designation=object.get_designation(),
                by_whom=object.get_by_whom())
            
            duty_obj= nurse_duty.objects.get(id=object.get_id())
            
        else:
             # Create new nurse duty record
            duty_obj=nurse_duty(
                date=object.get_date(),
                time=object.get_time(),
                person_details_id=object.get_person_details_id(),
                person_type=object.get_person_type(),
                duty_option=object.get_duty_option(),
                designation=object.get_designation(),
                by_whom=object.get_by_whom(),
                note=object.get_note())
            
            duty_obj.save()
            
        response =nurse_duty_response()
        response.set_id(duty_obj.id)
        response.set_date(str(duty_obj.date))
        response.set_time(str(duty_obj.time))
        response.set_duty_option(duty_obj.duty_option)
        response.set_person_details_id(duty_obj.person_details_id)
        response.set_person_type(duty_obj.person_type)
        response.set_status(duty_obj.status)
        response.set_note(duty_obj.note)
        response.set_designation(duty_obj.designation)
        response.set_by_whom(duty_obj.by_whom)
        
        return response
    
    
    
    def get_nurse_duty(self):
        condition=Q(status=1)
        obj_list = nurse_duty.objects.filter(condition)
        array_list=[]
        
        for obj in obj_list:
            response = nurse_duty_response()
            response.set_id(obj.id)
            response.set_date(str(obj.date))
            response.set_time(str(obj.time))
            response.set_person_details_id(obj.person_details_id)
            response.set_person_type(obj.person_type)
            response.set_duty_option(obj.duty_option)
            response.set_status(obj.status)
            response.set_note(obj.note)
            response.set_designation(obj.designation)
            response.set_by_whom(obj.by_whom)
            
            array_list.append(response.get())
        return JsonResponse(array_list, safe=False)
    
    def delete_nurse_duty(self,id):
        obj=nurse_duty.objects.filter(id=id).update(status=0)
        response=nurse_duty_response()
        return JsonResponse({"message": "Deleted Successfully"}, safe=False)
       
   
   # get count dutyoption 
            
    def count_duty_option(self):
        results = nurse_duty.objects.values('date').annotate(
            dressing_count=Count('date', filter= Q(duty_option='Dressing')),
            catheter_change_count=Count('date', filter= Q(duty_option='Catheter Change')),
            blood_presser_count=Count('date', filter= Q(duty_option='Blood Presser')),
            blood_sugar_count=Count('date', filter= Q(duty_option='Blood Sugar'))) .order_by('date')
        data = []
        
        for resultObj in results:
            response=dutyCountResponse()
            response.set_duty_date(str(resultObj['date']))
            response.set_dressing_count(str(resultObj['dressing_count']))
            response.set_catheter_change_count(str(resultObj['catheter_change_count']))
            response.set_blood_presser_count(str(resultObj['blood_presser_count']))
            response.set_blood_sugar_count(str(resultObj['blood_sugar_count']))
            data.append(response.get())
        return JsonResponse(data, safe=False)
        # return data      
            
            
            
        