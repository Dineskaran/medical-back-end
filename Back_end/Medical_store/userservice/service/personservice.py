from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q

from userservice.data.response.personresponse import person_details_response
from userservice.data.request.personrequest import person_details_request
from userservice.models import person_details

class person_detals_service:
    
    def insert_person(self, request: person_details_request):
        if request.get_id() is not None and request.get_id() != 0:
            # Update existing person record
            person_details.objects.filter(person_details_id=request.get_id()).update(
                person_type=request.get_person_type(),
                person_no=request.get_person_no(),
                first_name=request.get_first_name(),
                last_name=request.get_last_name(),
                date_of_birth=request.get_date_of_birth(),
                gender=request.get_gender(),
                civil_status=request.get_civil_status(),
                nic=request.get_nic(),
                effect=request.get_effect(),
                effect_type=request.get_effect_type(),
                effect_status=request.get_effect_status(),
                effect_reason=request.get_effect_reason(),
                effect_date=request.get_effect_date(),
                is_bed_sore=request.get_is_bed_sore(),
                contact_number=request.get_contact_number(),
                address=request.get_address(),
                district=request.get_district(),
                now_status=request.get_now_status(),
            
            )
            person_obj = person_details.objects.get(id=request.get_id())
            
        else:
            # Create new person record
            person_obj = person_details(
                person_type=request.get_person_type(),
                person_no=request.get_person_no(),
                first_name=request.get_first_name(),
                last_name=request.get_last_name(),
                date_of_birth=request.get_date_of_birth(),
                gender=request.get_gender(),
                civil_status=request.get_civil_status(),
                nic=request.get_nic(),
                effect=request.get_effect(),
                effect_type=request.get_effect_type(),
                effect_status=request.get_effect_status(),
                effect_reason=request.get_effect_reason(),
                effect_date=request.get_effect_date(),
                is_bed_sore=request.get_is_bed_sore(),
                contact_number=request.get_contact_number(),
                address=request.get_address(),
                district=request.get_district(),
                now_status=request.get_now_status(),
            
            )
            person_obj.save()
        
        response = person_details_response()
        response.set_id(person_obj.id)
        response.set_person_type(person_obj.person_type)
        response.set_person_no(person_obj.person_no)
        response.set_first_name(person_obj.first_name)
        response.set_last_name(person_obj.last_name)
        response.set_date_of_birth(str(person_obj.date_of_birth))
        response.set_gender(person_obj.gender)
        response.set_civil_status(person_obj.civil_status)
        response.set_nic(person_obj.nic)
        response.set_effect(person_obj.effect)
        response.set_effect_type(person_obj.effect_type)
        response.set_effect_status(person_obj.effect_status)
        response.set_effect_reason(person_obj.effect_reason)
        response.set_effect_date(str(person_obj.effect_date))
        response.set_is_bed_sore(person_obj.is_bed_sore)
        response.set_contact_number(person_obj.contact_number)
        response.set_address(person_obj.address)
        response.set_district(person_obj.district)
        response.set_now_status(person_obj.now_status)
        
        
        return response
    
    def get_persons(self,person_type):
        condition = Q(status=1)
        if person_type != "" and person_type != None:
            condition &= Q(person_type=person_type)
            
        obj_list = person_details.objects.filter(condition)
        array_list = []
        
        for obj in obj_list:
            response = person_details_response()
            response.set_id(obj.id)
            response.set_person_type(obj.person_type)
            response.set_person_no(obj.person_no)
            response.set_first_name(obj.first_name)
            response.set_last_name(obj.last_name)
            response.set_date_of_birth(str(obj.date_of_birth))
            response.set_gender(obj.gender)
            response.set_civil_status(obj.civil_status)
            response.set_nic(obj.nic)
            response.set_effect(obj.effect)
            response.set_effect_type(obj.effect_type)
            response.set_effect_status(obj.effect_status)
            response.set_effect_reason(obj.effect_reason)
            response.set_effect_date(str(obj.effect_date))
            response.set_is_bed_sore(str(obj.is_bed_sore))
            response.set_contact_number(obj.contact_number)
            response.set_address(obj.address)
            response.set_district(obj.district)
            response.set_now_status(obj.now_status)
            # response.set_status(obj.status)
            
            array_list.append(response.get())
        print(array_list)
        return JsonResponse(array_list, safe=False)
    
    def delete_person(self, id):
        person_details.objects.filter(id=id).update(status=0)
        return JsonResponse({"message": "Deleted Successfully"}, safe=False)
