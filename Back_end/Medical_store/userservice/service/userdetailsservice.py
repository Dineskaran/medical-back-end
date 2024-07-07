import re
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponse
from userservice.data.response.userdetailsresponse import user_details_response
from userservice.data.request.userdetailsrequest import user_details_request
from userservice.models import user_details
from rest_framework import status
from django.db.utils import IntegrityError


class user_details_service:
    
    def validate_password(self, password):
        if not (8 <= len(password) <= 16):
            return False, "Password must be between 8 and 16 characters long."
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter."
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter."
        if not re.search(r'[0-9]', password):
            return False, "Password must contain at least one number."
        if not re.search(r'[\W_]', password):  # \W matches any non-word character
            return False, "Password must contain at least one special character."
        return True, ""

    def insert_or_update_user(self, user_data):
        try:
            user_id = user_data.get('id', 0)
            
            if user_id and user_id != 0:
                # Update existing user record
                user_obj = user_details.objects.get(id=user_id)

                # Check if userid has changed and if new userid is available
                if user_obj.userid != user_data['userid']:
                    if user_details.objects.filter(userid=user_data['userid']).exists():
                        return {"status": 400, "error": "UserID already exists."}

                user_obj.userid = user_data['userid']
                user_obj.user_name = user_data['user_name']
                user_obj.privilege = user_data['privilege']
                user_obj.save()
                # message = "User updated successfully."

            else:
                # Validate password for new user
                password_valid, message = self.validate_password(user_data.get('password', ''))
                if not password_valid:
                    return {"status": 400, "error": message}

                # Create new user record
                hashed_password = make_password(user_data['password'])
                user_obj = user_details.objects.create(
                    userid=user_data['userid'],
                    user_name=user_data['user_name'],
                    password=hashed_password,
                    privilege=user_data['privilege'],
                    create_by=user_data.get('create_by', '')
                )
                # message = "User created successfully."

            response_data = {
                "id": user_obj.id,
                "userid": user_obj.userid,
                "user_name": user_obj.user_name,
                "privilege": user_obj.privilege,
                "create_date": str(user_obj.create_date),
                "create_by": user_obj.create_by,
                "message": message,
                "status": 200
            }

            return response_data

        except IntegrityError:
            return {"status": 400, "error": "UserID already exists."}
        except Exception as e:
            return { "": str(e)}


    def check_userid_availability(self, userid):
        try:
            if user_details.objects.filter(userid=userid).exists():
                return {"available": False, "status": 200}
            return {"available": True, "status": 200}
        except Exception as e:
            return {"status": 500, "error": str(e)}
        
    def get_users(self):
        try:
            condition = user_details.objects.filter(status=1)
            array_list = []
            for user_obj in condition:
                response = user_details_response()
                response.set_id(user_obj.id)
                response.set_userid(user_obj.userid)
                response.set_user_name(user_obj.user_name)
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
            response = user_details_response()
            array_list = []
            if user_obj and check_password(old_password, user_obj.password):
                password_valid, message = self.validate_password(new_password)
                if not password_valid:
                    response.set_status("Invalid password")
                    return JsonResponse(array_list, safe=False)
                encrypted_password = make_password(new_password)
                user_obj.password = encrypted_password
                user_obj.save()
                response.set_status("changed successfully")
                array_list.append(response.get())
                return JsonResponse(array_list, safe=False)
                
                # return JsonResponse({"message": "changed successfully"}, safe=False)
            else:
                # return JsonResponse({"error": "Invalid old password"}, status=400, safe=False)
                response.set_status("Invalid password")
                array_list.append(response.get())
                return JsonResponse(array_list, safe=False)
        except user_details.DoesNotExist:
            # return JsonResponse({"error": "User not found"}, status=404, safe=False)
            response.set_status("Invalid userid")
            array_list.append(response.get())
            return JsonResponse(array_list, safe=False)

    def authenticate_user(self, userid, password):
        user_obj = user_details.objects.filter(userid=userid)
        response = user_details_response()
        array_list = []
        if user_obj:
            if check_password(password, user_obj[0].password):     
                for obj in user_obj:
                    response.set_id(obj.id)
                    response.set_userid(obj.userid)
                    response.set_user_name(obj.user_name)
                    response.set_privilege(obj.privilege)
                    response.set_status("Success")
                    array_list.append(response.get())
                return JsonResponse(array_list, safe=False)
                    
            else:
                response.set_status("Invalid password")
                array_list.append(response.get())
                return JsonResponse(array_list, safe=False)
        else:
            response.set_status("Invalid userid")
            array_list.append(response.get())
            return JsonResponse(array_list, safe=False)
        print(user_obj)
