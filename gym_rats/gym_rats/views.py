from django.shortcuts import render
from django.http import JsonResponse

def my_endpoint(request):
    data = {'key': 'value'}
    return JsonResponse(data)