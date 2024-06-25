import json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from userservice.data.request.userdetailsrequest import user_details_request
from userservice.service.userdetailsservice import user_details_service

@csrf_exempt
@api_view(['POST', 'GET'])
def insert_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        admin_id = request.user.id
        user_request = user_details_request(data)
        # print("check user",user_request)
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