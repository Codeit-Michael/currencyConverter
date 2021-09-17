from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import converterForm

# Create your views here.
def convert(request):
	myForm = converterForm()
	response = requests.get("https://api.exchangerate.host/latest")
	myJson = response.json()
	currs = myJson['rates']

	return render(request,'converter/home.html',{'currs':currs, 'myForm':myForm})