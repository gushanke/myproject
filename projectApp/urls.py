from django.urls import path
from . import views
 
urlpatterns = [
    path('testapi', views.testapi, name='testapi'),
]
