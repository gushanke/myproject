# from django.shortcuts import render
from django.shortcuts import render
 
# Create your views here.
# from django.http import HttpResponse
# import json
 
# # 解决前端post请求 csrf问题
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
 
# def testapi(request):
# 	print(request)
# 	print(request.method)
# 	if request.method == "GET":
# 		print(request.GET.get('aa'))
# 		resp = {'errorcode': 100, 'type': 'Get', 'data': {'main': request.GET.get('aa')}}
# 		return HttpResponse(json.dumps(resp), content_type="application/json")
# 	else:
# 		print(request.POST)
# 		print(request.body)
# 		str1=str(request.body, encoding = "utf-8")  
# 		data=eval(str1)
# 		print(data)
# 		print(data['aa'])
# 		print(type(request.body))
# 		resp = {'errorcode': 100, 'type': 'Post', 'data': {'main': data['aa']}}
# 		return HttpResponse(json.dumps(resp), content_type="application/json")
# from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
 
from .models import Book
# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
 
 
@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
