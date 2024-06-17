import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from userservice.data.request.userdetailsrequest import user_details_request
from userservice.service.userdetailsservice import user_details_service

@csrf_exempt
@api_view(['POST', 'GET'])
def insert_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_request = user_details_request(data)
        print("check user",user_request)
        service = user_details_service()
        response = service.insert_user(user_request)
        return HttpResponse(response.get(), content_type='application/json')
    else:
        service = user_details_service()
        response = service.get_users()
        return HttpResponse(response, content_type='application/json')

@csrf_exempt
@api_view(['GET', 'DELETE'])
def manage_user(request):
    id = request.GET.get("id")
    if request.method == "GET":
        service = user_details_service()
        response = service.get_users()
        return HttpResponse(response, content_type='application/json')
    
    elif request.method == "DELETE":
        service = user_details_service()
        response = service.delete_user(id)
        return HttpResponse(response, content_type='application/json')
