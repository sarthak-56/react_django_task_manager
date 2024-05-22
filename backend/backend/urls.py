from django.contrib import admin
from todo import views                       
from rest_framework import routers                 
from django.urls import path, include                

router = routers.DefaultRouter()                   
router.register(r'tasks', views.TodoView, 'task')   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))          

