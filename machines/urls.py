from django.conf.urls import url
from django.urls import include, path
from . import views , api


app_name='machines'

urlpatterns = [
    
    url(r'^$', views.all_machines , name='all_machines'),

    path('api/list', api.MachinesList , name='MachinesList'),


]