from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
	data = {"Message": "Hello World!"}
# should access Model objects and use Templates to prepare responses.
	return JsonResponse(data)

