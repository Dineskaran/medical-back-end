from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models import Count


from userservice.data.response.nurseresponse import nurse_duty_response,dutyCountResponse,nurse_duty_report_response
from userservice.data.request.nurserequest import nurse_duty_request
from userservice.models import nurse_duty,person_details

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
        condition = Q(status=1)
        obj_list = nurse_duty.objects.filter(condition).select_related('person_details')
        array_list = []
        
        for obj in obj_list:
            response = nurse_duty_response()
            response.set_id(obj.id)
            response.set_date(str(obj.date))
            response.set_time(str(obj.time))
            response.set_person_details_id(obj.person_details_id)
            response.set_person_details_first_name(obj.person_details.first_name)
            response.set_person_details_last_name(obj.person_details.last_name)
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
            
    def count_duty_option(self,start_date_str, end_date_str):
        # Convert string dates to datetime objects
        try:
            # Attempt to parse in '%d-%m-%Y' format
            start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
            end_date = datetime.strptime(end_date_str, '%d-%m-%Y').date()
        except ValueError:
            try:
                # Attempt to parse in '%Y-%m-%d' format
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({"error": "Incorrect date format, should be either DD-MM-YYYY or YYYY-MM-DD"}, status=400)
        # Filter nurse_duty records based on date range
        
        condition=Q(status=1)
        
        results = nurse_duty.objects.filter(condition,date__range=(start_date, end_date)
                                            ).values('date').annotate(
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
    
    
    

    def nurse_duty_report_by_option(self, duty_option):
        condition = Q(status=1) & Q(duty_option=duty_option)
        
        # Query nurse_duty records with status=1 and the specified duty_option, joining with person_details
        results = nurse_duty.objects.filter(condition).values(
            'person_details__id',
            'person_details__first_name',
            'person_details__last_name',
            'person_details__gender',
            'person_details__district'
        ).annotate(
            duty_count=Count('duty_option'),
            male_count=Count('duty_option', filter=Q(person_details__gender='male')),
            female_count=Count('duty_option', filter=Q(person_details__gender='Female')),
        ).order_by('person_details__first_name', 'person_details__last_name')

        data = []

        for result in results:
            response = nurse_duty_report_response()
            response.set_person_id(result['person_details__id'])
            response.set_first_name(result['person_details__first_name'])
            response.set_last_name(result['person_details__last_name'])
            response.set_gender(result['person_details__gender'])
            response.set_district(result['person_details__district'])
            response.set_duty_count(result['duty_count'])
            response.set_male_count(result['male_count'])
            response.set_female_count(result['female_count'])

            # Assign total_count directly if supported by your response class
            response.total_count = result['duty_count']

            data.append(response.get())

        return JsonResponse(data, safe=False)

