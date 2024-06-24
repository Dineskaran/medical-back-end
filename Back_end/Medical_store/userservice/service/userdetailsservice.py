from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
import datetime
from userservice.data.response.userdetailsresponse import user_details_response
from userservice.data.request.userdetailsrequest import  user_details_request
from userservice.models import user_details

from django.contrib.auth.hashers import make_password, check_password




class user_details_service:

    def insert_user(self, user_data):
        try:
            if user_data.get_id() is not None and user_data.get_id() != 0:
                # Update existing user record
                user_obj = user_details.objects.get(id=user_data.get_id())
                user_obj.userid = user_data.get_userid()
                user_obj.user_name = user_data.get_user_name()
                user_obj.privilege = user_data.get_privilege()
                user_obj.save()
            else:
                # Create new user record
                encrypted_password = make_password(user_data.get_password())
                user_obj = user_details.objects.create(
                    userid=user_data.get_userid(),
                    user_name=user_data.get_user_name(),
                    password=encrypted_password,
                    privilege=user_data.get_privilege(),
                    # Assuming create_date and create_by are handled elsewhere
                )
            
            response = user_details_response()
            response.set_id(user_obj.id)
            response.set_userid(user_obj.userid)
            response.set_user_name(user_obj.user_name)
            response.set_password("")  # Do not send password in response for security reasons
            response.set_privilege(user_obj.privilege)
            response.set_create_date(str(user_obj.create_date))
            response.set_create_by(user_obj.create_by)

            return response

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500, safe=False)

    def get_users_byid(self, id):
        try:
            user_obj = user_details.objects.get(id=id)
            response = user_details_response()
            response.set_id(user_obj.id)
            response.set_userid(user_obj.userid)
            response.set_user_name(user_obj.user_name)
            response.set_password("")  # Do not send password in response for security reasons
            response.set_privilege(user_obj.privilege)
            response.set_create_date(str(user_obj.create_date))
            response.set_create_by(user_obj.create_by)
            return response
        except user_details.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404, safe=False)

    def get_users(self):
        try:
            condition = user_details.objects.filter(status=1)
            array_list = []
            for obj in condition:
                response = user_details_response()
                response.set_id(obj.id)
                response.set_userid(obj.userid)
                response.set_user_name(obj.user_name)
                response.set_password("")  
                response.set_privilege(obj.privilege)
                response.set_create_date(str(obj.create_date))
                response.set_create_by(obj.create_by)
                array_list.append(response.get())
            return JsonResponse(array_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500, safe=False)

    def delete_user(self, id):
        try:
            user_details.objects.filter(id=id).update(status=0)
            return JsonResponse({"message": f"user_id :{id} Successfully Deleted"}, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500, safe=False)

    def change_password(self, user_id, old_password, new_password):
        try:
            user_obj = user_details.objects.get(id=user_id)
            if check_password(old_password, user_obj.password):
                encrypted_password = make_password(new_password)
                user_obj.password = encrypted_password
                user_obj.save()
                return JsonResponse({"message": "Password changed successfully"}, safe=False)
            else:
                return JsonResponse({"error": "Old password is incorrect"}, status=400, safe=False)
        except user_details.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404, safe=False)

    def authenticate_user(self, user_name, password):
        try:
            user_obj = user_details.objects.get(userid=user_name)
            if check_password(password, user_obj.password):
                return JsonResponse({"message": "Login successful"}, safe=False)
            else:
                return JsonResponse({"error": "Invalid username or password"}, status=400, safe=False)
        except user_details.DoesNotExist:
            return JsonResponse({"error": "Invalid username or password"}, status=400, safe=False)
