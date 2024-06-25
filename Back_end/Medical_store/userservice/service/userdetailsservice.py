from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from userservice.data.response.userdetailsresponse import user_details_response
from userservice.data.request.userdetailsrequest import user_details_request
from userservice.models import user_details
from rest_framework import status

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
                hashed_password = make_password(user_data.get_password())
                user_obj = user_details.objects.create(
                    userid=user_data.get_userid(),
                    user_name=user_data.get_user_name(),
                    password=hashed_password,
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
            for user_obj in condition:
                response = user_details_response()
                response.set_id(user_obj.id)
                response.set_userid(user_obj.userid)
                response.set_user_name(user_obj.user_name)
                response.set_password("")  
                response.set_privilege(user_obj.privilege)
                response.set_create_date(str(user_obj.create_date))
                response.set_create_by(user_obj.create_by)
                array_list.append(response.get())
            return JsonResponse(array_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500, safe=False)

    def delete_user(self, id):
        try:
            user_details.objects.filter(id=id).update(status=0)
            return JsonResponse({"message": f"userid :{id} Successfully Deleted"}, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500, safe=False)

    def change_password(self, userid, old_password, new_password):
        try:
            user_obj = user_details.objects.filter(userid=userid).first()
            if user_obj and check_password(old_password, user_obj.password):
                encrypted_password = make_password(new_password)
                user_obj.password = encrypted_password
                user_obj.save()
                return JsonResponse({"message": "Password changed successfully"}, safe=False)
            else:
                return JsonResponse({"error": "Invalid old password"}, status=400, safe=False)
        except user_details.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500, safe=False)
        
        

    def authenticate_user(self, userid, password):
        # try:
            user_obj = user_details.objects.filter(userid=userid)
            response = user_details_response()
            array_list = []
            if user_obj:
                if check_password(password,user_obj[0].password):     
                    # return JsonResponse({"message": "Login successful"}, safe=False)
                    
                    for obj in user_obj:
                        # response = user_details_response()
                        response.set_id(obj.id)
                        response.set_userid(obj.userid)
                        response.set_user_name(obj.user_name)
                        # response.set_password("")  
                        response.set_privilege(obj.privilege)
                        # response.set_create_date(str(obj.create_date))
                        # response.set_create_by(obj.create_by)
                        response.set_status("Success")
                        array_list.append(response.get())
                    return JsonResponse(array_list, safe=False)
                        
                else:
                       # response = user_details_response()
                        # response.set_id(obj.id)
                        # response.set_userid(obj.userid)
                        # response.set_user_name(obj.user_name)
                        # response.set_privilege(obj.privilege)
                        response.set_status("Invalid password")
                        array_list.append(response.get())
                        return JsonResponse(array_list, safe=False)
                    # return JsonResponse({"error": "Invalid password"}, status=401, safe=False)
            else:
                response.set_status("Invalid userid")
                array_list.append(response.get())
                return JsonResponse(array_list, safe=False)
                # return JsonResponse({"error": "Invalid username"}, status=400, safe=False)
            print(user_obj)
        # except user_details.DoesNotExist:
        #     return JsonResponse({"error": "Invalid username or password"}, status=400, safe=False)
        
        