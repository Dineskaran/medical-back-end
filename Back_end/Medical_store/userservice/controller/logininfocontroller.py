import json
import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


from userservice.data.request.logininforequest import login_info_request
from userservice.service.logininfoservice import login_info_service


@csrf_exempt
@api_view(['POST','GET'])
def insert_log(request):
    if request.method=='POST':
        data=json.loads(request.body)
        
        log_request=login_info_request(data)
        print("call from login form",log_request)
        log_servise=login_info_service()
        response=log_servise.insert_log_entry(log_request)
        # print("Response to login form",log_request)
        # return HttpResponse(response,content_type='application/json')
        return HttpResponse(response)
    
    else:
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        log_servise=login_info_service()
        response=log_servise.get_log_entries(start_date,end_date)  
        print("Response to login info form",response) 
        return HttpResponse(response,content_type='application/json')
    
    

@csrf_exempt
@api_view(['DELETE'])
def delete_log_details(request):
    id=request.GET.get("id")
    
    if request.method=="DELETE":
        log_servise = login_info_service()
        id=request.GET.get("id")
        response = log_servise.delete_log_entry(id)
        return HttpResponse(response,content_type='application/json')