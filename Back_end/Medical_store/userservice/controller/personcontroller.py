import json
import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from userservice.data.request.personrequest import person_details_request
from userservice.service.personservice import person_detals_service



@csrf_exempt
@api_view(['POST','GET'])
def insert_prson_details(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(data)
        person_request=person_details_request(data)
        service= person_detals_service()
        response=service.insert_person(person_request)
        return HttpResponse(response.get(),content_type='application/json')
    
    else:
        print("call from person_service component")
        person_type = request.GET.get("person_type")
        service= person_detals_service()
        response=service.get_persons(person_type)  
        return HttpResponse(response,content_type='application/json')
    
@csrf_exempt
@api_view(['DELETE'])
def delete_person_details(request):
    person_details_id=request.GET.get("person_details_id")
    if request.method=="DELETE":
        service = person_detals_service()
        person_details_id=request.GET.get("person_details_id")
        response =service.delete_person(id)
        return HttpResponse(response,content_type='application/json')