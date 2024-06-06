
from django.contrib import admin
from django.urls import path, include
from userservice.controller import usercontroller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userservice/', include('userservice.urls'))
]
