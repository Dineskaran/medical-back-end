from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User


from userservice.data.response.logininforesponse import login_info_response
from userservice.data.request.logininforequest import login_info_request
from userservice.models import login_info

class login_info_service:

    def insert_log_entry(self, object):
        # request = login_info_request(request_data)
        
        if object.get_id() is not None and object.get_id() != 0:
            # Update existing log entry
            obj1=login_info.objects.filter(id=object.get_id()).update(
                user_details_id=object.get_user_details_id(),
                log_date=object.get_log_date(),
                log_time=object.get_log_time(),
                location=object.get_location(),
                log_out_time=object.get_log_out_time(),
                num_of_attempt=object.get_num_of_attempt(),
                # log_status=object.get_log_status(),
                # status=request.get_status()
            )
            obj = login_info.objects.get(id=object.get_id())
        else:
            # Create new log entry
            obj = login_info(
                user_details_id=object.get_user_details_id(),
                log_date=object.get_log_date(),
                log_time=object.get_log_time(),
                location=object.get_location(),
                log_out_time=object.get_log_out_time(),
                num_of_attempt=object.get_num_of_attempt(),
                # log_status=object.get_log_status(),
                # status=request.get_status()
            )
            obj.save()
        
        response = login_info_response()
        response.set_id(obj.id)
        response.set_user_details_id(obj.user_details_id)
        response.set_log_date(str(obj.log_date))
        response.set_log_time(str(obj.log_time))
        response.set_location(obj.location)
        response.set_log_out_time(str(obj.log_out_time))
        response.set_num_of_attempt(obj.num_of_attempt)
        response.set_log_status(obj.log_status)
        response.set_status(obj.status)
        
        return response.get()
    
    def get_log_entries(self):
        condition = Q(status=1)  # Assuming 'active' status means it's not deleted
        obj_list = login_info.objects.filter(condition)
        response_list = []
        
        for obj in obj_list:
            response = login_info_response()
            response.set_id(obj.id)
            response.set_user_details_id(obj.user_details_id)
            response.set_log_date(str(obj.log_date))
            response.set_log_time(str(obj.log_time))
            response.set_location(obj.location)
            response.set_log_out_time(str(obj.log_out_time))
            response.set_num_of_attempt(obj.num_of_attempt)
            response.set_log_status(obj.log_status)
            response.set_status(obj.status)
            
            response_list.append(response.get())
        return JsonResponse(response_list, safe=False)

    def delete_log_entry(self, id):
        obj=login_info.objects.filter(id=id).update(status=0)  # Assuming 'inactive' status means it's deleted
        response= login_info_response()
        return JsonResponse({"message": "Deleted Successfully"}, safe=False)
