from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
import datetime


from userservice.data.response.dropdownresponce import dropdown_response
from userservice.data.request.dropdownrequest import dropdown_request
from userservice.models import dropdown_table

class dropdown_service:
    
    def insert_dropdown(self,object):
        if object.get_id() is not None and object.get_id() != 0:
            obj = dropdown_table.objects.get(id=object.get_id())
            obj.list_type = object.get_list_type()
            obj.list_value = object.get_list_value()
            obj.filter_by = object.get_filter_by()
            
            obj.save()
        else:
            obj = dropdown_table(
                list_type = object.get_list_type(),
                list_value = object.get_list_value(),
                filter_by = object.get_filter_by(), 
            )   
            obj.save()
            
        response = dropdown_response()
        response.set_id(obj.id)
        response.set_list_type(obj.list_type)
        response.set_list_value(obj.list_value)    
        response.set_filter_by(obj.filter_by)
         
        
        return response
    
     
    def get_dropdown(self, list_type,filter_by):
        condition = Q(status=1)
        if list_type != "" and list_type != None:
            condition &= Q(list_type=list_type)
                    
        if filter_by != "" and filter_by != None:
            condition &= Q(filter_by=filter_by)
                    
        dropdown_list = dropdown_table.objects.filter(condition)
        print(dropdown_list.query)
        array=[]
        for obj in dropdown_list:
            response = dropdown_response()
            response.set_id(obj.id)
            response.set_list_type(obj.list_type)
            response.set_list_value(obj.list_value)
            response.set_filter_by(obj.filter_by)
            response.set_status(obj.status)
            array.append(response.get())

        # return array
        return JsonResponse(array, safe=False)
    
    def delete_dropdown(self,id):
        obj = dropdown_table.objects.filter(id=id).update(status=0)
        response = dropdown_response()
        response.set_id("CATEGORY DELETED" +str(id))
        print("SUCCESSFULLY CATEGORY DELETED")
        return response
    