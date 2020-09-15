from django.conf.urls import url
from django.urls import include, path
from . import views , api


app_name='pods'

urlpatterns = [
    
    url(r'^$', views.all_pods , name='all_pods'),
    path('api/list', api.PodsList , name='PodsList'),



]