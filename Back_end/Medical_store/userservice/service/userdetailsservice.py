from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
import datetime

from userservice.data.response.userdetailsresponse import user_details_response
from userservice.data.request.userdetailsrequest import  user_details_request
from userservice.models import user_details


class user_details_service:
    
    def insert_user(self, user_data):
        if user_data.get_id() is not None and user_data.get_id() != 0:
            # Update existing user record
            user_details.objects.filter(id=user_data.get_id()).update(
                user_id=user_data.get_user_id(),
                user_name=user_data.get_user_name(),
                password=user_data.get_password(),
                privilege=user_data.get_privilege(),
                create_date=user_data.get_create_date(),
                create_by=user_data.get_create_by(),
                # status=user_data.status()
            )
            
            user_obj = user_details.objects.get(id=user_data.get_user_id())
            
        else:
            # Create new user record
            user_obj = user_details.objects.create(
                user_id=user_data.get_user_id(),
                user_name=user_data.get_user_name(),
                password=user_data.get_password(),
                privilege=user_data.get_privilege(),
                create_date=user_data.get_create_date(),
                create_by=user_data.get_create_by(),
                # status=user_data.status()
            )
        
        response = user_details_response()
        response.set_id(user_obj.id)
        response.set_user_id(user_obj.user_id)
        response.set_user_name(user_obj.user_name)
        response.set_password(user_obj.password)  
        response.set_privilege(user_obj.privilege)
        response.set_create_date(str(user_obj.create_date))
        response.set_create_by(user_obj.create_by)
        # response.set_status(user_obj.status)
        
        return response

    def get_users(self):
        condition = Q(status=1)
        user_list = user_details.objects.filter(condition)
        array_list = []
        
        for obj in user_list:
            response = user_details_response()
            response.set_id(obj.id)
            response.set_user_id(obj.user_id)
            response.set_user_name(obj.user_name)
            response.set_password(obj.password)  
            response.set_privilege(obj.privilege)
            response.set_create_date(str(obj.create_date))
            response.set_create_by(obj.create_by)
            response.set_status(obj.status)
            
            array_list.append(response.get())
        
        return JsonResponse(array_list, safe=False)

    def delete_user(self, id):
        user_details.objects.filter(id=id).update(status=0)
        return JsonResponse({"message": f"user_id :{id} Successfully Deleted"}, safe=False)
