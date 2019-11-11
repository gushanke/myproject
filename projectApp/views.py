# from django.shortcuts import render
from django.shortcuts import render
 
# Create your views here.
from django.http import HttpResponse
import json
 
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
 
def testapi(request):
	print(request)
	print(request.method)
	if request.method == "GET":
		print(request.GET.get('aa'))
		resp = {'errorcode': 100, 'type': 'Get', 'data': {'main': request.GET.get('aa')}}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		print(request.POST)
		print(request.body)
		str1=str(request.body, encoding = "utf-8")  
		data=eval(str1)
		print(data)
		print(data['aa'])
		print(type(request.body))
		resp = {'errorcode': 100, 'type': 'Post', 'data': {'main': data['aa']}}
		return HttpResponse(json.dumps(resp), content_type="application/json")