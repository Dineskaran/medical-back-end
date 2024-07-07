import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db import IntegrityError
from userservice.data.request.userdetailsrequest import user_details_request
from userservice.service.userdetailsservice import user_details_service

@api_view(['POST', 'GET'])
@csrf_exempt
def insert_user(request):
    service = user_details_service()

    if request.method == 'POST':
        data = request.data
        response = service.insert_or_update_user(data)
        
        # Check the type of response and handle accordingly
        if 'error' in response:
            return JsonResponse({"error": response['error']}, status=400)
        else:
            return JsonResponse(response, status=200)  # Ensure status is integer

    elif request.method == 'GET':
        response = service.get_users()
        return HttpResponse(response, content_type='application/json')

@api_view(['GET'])
@csrf_exempt
def check_userid(request):
    service = user_details_service()
    userid = request.GET.get('userid')
    response = service.check_userid_availability(userid)
    return JsonResponse(response, status=response['status'])

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


@csrf_exempt
@api_view(['POST'])
def change_password(request):
    data = json.loads(request.body)
    user_id = data.get("userid")
    old_password = data.get("old_password")
    new_password = data.get("new_password")
    service = user_details_service()
    response = service.change_password(user_id, old_password, new_password)
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
@api_view(['GET'])
def login(request):
    # data = json.loads(request.body)
    userid = request.GET.get("userid")
    plainpassword = request.GET.get("password")
    print(userid, "check pass: ",plainpassword)
    service = user_details_service()
    response = service.authenticate_user(userid, plainpassword)
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
@api_view(['POST'])
def block_user(request):
    user_id = request.data.get('userid')
    try:
        user = user_details.objects.get(id=user_id)
        user.status = 'blocked'  # Adjust this based on your user_details model fields
        user.save()
        return JsonResponse({'message': 'User blocked successfully'}, status=200)
    except user_details.DoesNotExist:
        return JsonResponse({'message': 'User not found'}, status=404)



# @csrf_exempt
# @api_view(['POST','GET'])
# def registLogin(request):
#     if request.method=="POST":
#         data=json.loads(request.body)
#         print(data)
#         userRequest=user_details_request(data)
#         service = user_details_service()
#         response = service.create_user(userRequest)
#         return HttpResponse(response.get(), content_type='application/json')
        
    
#     else:
#         userid=request.GET.get("userid") 
#         password=request.GET.get("password")          
#         service = user_details_service() 
#         response = service.login(userid,password)
#         return HttpResponse(response, content_type='application/json')