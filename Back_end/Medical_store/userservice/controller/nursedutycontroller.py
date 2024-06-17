import json
import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


from userservice.data.request.nurserequest import nurse_duty_request
from userservice.service.nurseservice import nurse_duty_service


@csrf_exempt
@api_view(['POST','GET'])
def insert_nurse_duty_details(request):
    if request.method=='POST':
        data=json.loads(request.body)
        # print(data)
        nurse_request=nurse_duty_request(data)
        nurse_servise=nurse_duty_service()
        response=nurse_servise.insert_nurse_duty(nurse_request)
        return HttpResponse(response.get(),content_type='application/json')
    
    else:
        # print("call from nurse_duty component")
        nurse_servise=nurse_duty_service()
        response=nurse_servise.get_nurse_duty()   # this get_nurse_duty()  getting nurseservise in to get_nurse_duty no 51
        return HttpResponse(response,content_type='application/json')
    
@csrf_exempt
@api_view(['DELETE'])
def delete_nurse_duty_details(request):
    id=request.GET.get("id")
    
    if request.method=="DELETE":
        nurse_servise = nurse_duty_service()
        id=request.GET.get("id")
        response = nurse_servise.delete_nurse_duty(id)
        return HttpResponse(response,content_type='application/json')