from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from userservice.data.response.logininforesponse import login_info_response
from userservice.data.request.logininforequest import login_info_request
from userservice.models import login_info
from datetime import datetime, timedelta


class login_info_service:

    def insert_log_entry(self, object):
        import datetime
        print("LOGIN INFO INSERT")
        try:
            if object.get_id() is not None and object.get_id() != 0:
                # Update existing log entry
                login_info.objects.filter(id=object.get_id()).update(
                    log_out_time=datetime.datetime.now().time()
                )
                obj = login_info.objects.get(id=object.get_id())
                
            else:
                # Create new log entry
                obj = login_info(
                    user_details_id=object.get_user_details_id(),
                    log_date=datetime.datetime.now(),
                    userid=object.get_userid(),
                    log_time=datetime.datetime.now().time(),
                    location=object.get_location(),
                    log_out_time=object.get_log_out_time(),
                    num_of_attempt=object.get_num_of_attempt(),
                    log_status=object.get_log_status(),
                )
                obj.save()
            
            response = login_info_response()
            response.set_id(obj.id)
            response.set_user_details_id(obj.user_details_id)
            response.set_userid(obj.userid)
            response.set_log_date(str(obj.log_date))
            response.set_log_time(str(obj.log_time))
            response.set_location(obj.location)
            response.set_log_out_time(str(obj.log_out_time))
            response.set_num_of_attempt(obj.num_of_attempt)
            response.set_log_status(obj.log_status)
            
            # return response.get()
            
            return obj.id
        
        except Exception as e:
            print("INSERT ERROR IS ",e)
            return JsonResponse({"error": str(e)}, status=500)

    def get_log_entries(self,start_date=None, end_date=None):
        # print("LOGIN INFO load service is called")
        try:
            condition = Q()  # Start with an empty condition

            # Apply date range condition if both start_date and end_date are provided
            if start_date and end_date:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
                condition &= Q(log_date__range=(start_date, end_date))

            # Query for log entries filtered by condition, ordered by log_date and log_time
            obj_list = login_info.objects.filter(condition).order_by('-log_date', '-log_time')

            # Limit result if start_date and end_date are not provided
            if not start_date and not end_date:
                obj_list = obj_list[:12]

            response_list = []

            for obj in obj_list:
                response = login_info_response()
                response.set_id(obj.id)
                response.set_user_details_id(obj.user_details_id)
                response.set_userid(obj.userid)
                response.set_log_date(str(obj.log_date))
                response.set_log_time(str(obj.log_time))
                response.set_location(obj.location)
                response.set_log_out_time(str(obj.log_out_time))
                response.set_num_of_attempt(obj.num_of_attempt)
                response.set_log_status(obj.log_status)

                response_list.append(response.get())

            return JsonResponse(response_list, safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    def delete_log_entry(self, id):
        try:
            login_info.objects.filter(id=id).update(status=0)  # Assuming 'inactive' status means it's deleted
            return JsonResponse({"message": "Deleted Successfully"}, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
