import json
from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


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
        start_date = request.GET.get('start_date_str')
        end_date = request.GET.get('end_date_str')
        # print("call from nurse_duty component")
        nurse_servise=nurse_duty_service()
        response = nurse_servise.get_nurse_duty(start_date, end_date) # this get_nurse_duty()  getting nurseservise in to get_nurse_duty no 51
        return HttpResponse(response,content_type='application/json')
    
    
    # count_duty_option
@csrf_exempt
@api_view(['GET'])
def duty_option_count_details(request):
    if request.method=='GET':
        start_date_str = request.GET.get('start_date_str')
        end_date_str = request.GET.get('end_date_str')
        nurse_servise=nurse_duty_service()
        response=nurse_servise.count_duty_option(start_date_str, end_date_str)
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
    
    
    
@csrf_exempt
@api_view(['GET'])
def nurse_duty_report_details(request):
    if request.method=='GET':
        duty_option = request.GET.get('duty_option')
        if duty_option:
            nurse_servise = nurse_duty_service()
            response = nurse_servise.nurse_duty_report_by_option(duty_option)
            return HttpResponse(response, content_type='application/json')
        
        return HttpResponse(json.dumps({"error": "duty_option parameter is required"}), content_type='application/json', status=400)