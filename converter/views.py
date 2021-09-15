from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def cur(request):
	response = requests.get("https://api.exchangerate.host/latest")