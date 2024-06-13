import json
import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


from userservice.data.request.logininforequest import login_info_request
from userservice.service.logininfoservice import login_info_service


@csrf_exempt
@api_view(['POST','GET'])
def insert_log_entry(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(data)
        log_request=login_info_request(data)
        log_servise=login_info_service()
        response=log_servise.insert_log_entry(log_request)
        return HttpResponse(response.get(),content_type='application/json')
    
    else:
        print("call from nurse_duty component")
        log_servise=login_info_service()
        response=log_servise.get_log_entries()   
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