import json
import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


from userservice.data.request.userrequest import home_admission_request, dropdown_request
from userservice.service.medicalservice import home_admission_service


# from userservice.utils import get_token
# from userservice.utls.medicalutlls import utlis




@csrf_exempt
@api_view(['POST','GET'])
def insert_homeadmission(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(data)
        homeadmission_request=home_admission_request(data)  # get home_admission_request from user service request  
        service=home_admission_service()
        response=service.insert_home_admission(homeadmission_request)            # insert_home_admission is get servise 
        return HttpResponse(response.get(),content_type='application/json')
    
    else:
        print("call from home admission component ")
        service=home_admission_service()
        response= service.get_home_admission_details()
        return HttpResponse(response,content_type='application/json')
        
        
   
#id used to get the details to the database

@csrf_exempt
@api_view(['GET','DELETE'])
def retrify_home_admission(request):
    id=request.GET.get("id")
    print("Controller Id ",id)
    if request.method == "GET":       
        service = home_admission_service()
        id=request.GET.get("id")
        response = service.get_home_admission_details()
        return HttpResponse(response, content_type='application/json')
    
    if request.method=="DELETE":
        service=home_admission_service()
        id=request.GET.get("id")
        
        response=service.delete_home_admission(id)
        return HttpResponse(response.get(),content_type='application/json')


@csrf_exempt
@api_view(['GET'])
def drop_down(request):
    if request.method=='GET':
        key = request.GET.get("key")
        query=request.GET.get("query")
        utlis_service=home_admission_service()
        obj=utlis_service.drop_down(key,query)
        return HttpResponse(obj, content_type='application/json')