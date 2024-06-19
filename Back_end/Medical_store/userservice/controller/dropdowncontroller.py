import json
import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from userservice.data.request.dropdownrequest import dropdown_request
from userservice.service.dropdownservice import dropdown_service



@csrf_exempt
@api_view(['POST','GET'])
def insert_dropdown(request):
    if request.method =='POST':
        data =json.loads(request.body)
        print(data)
        dropdowns_request = dropdown_request(data)    
        service = dropdown_service()
        response = service.insert_dropdown(dropdowns_request)         
        return HttpResponse(response.get(),content_type='application/json')
    
    else:
        print("call from dropdown component ")
        service= dropdown_service()
        list_type = request.GET.get("list_type")
        value_filter = request.GET.get("filter_by")
        print("this is list type", list_type)
        print("this is value filter", value_filter)
        response= service.get_dropdown(list_type,value_filter)
        return HttpResponse(response,content_type='application/json')
    
    



@csrf_exempt
@api_view(['GET'])
def drop_down_distin(request):
    if request.method=='GET':
        utlis_service= dropdown_service()
        response=utlis_service.get_distinList()
        return HttpResponse(response,content_type='application/json')
 
 
@csrf_exempt
@api_view(['DELETE'])
def delete_drop_down(request):   
    id=request.GET.get("id")
    if request.method =="DELETE":
        service = dropdown_service()
        id = request.GET.get("id")
        response = service.delete_dropdown(id)
        return HttpResponse(response.get(),content_type='application/json')
