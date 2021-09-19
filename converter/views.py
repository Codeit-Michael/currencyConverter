from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import converterForm

# Create your views here.
def convert(request):
	converted_amount = 0
	response = requests.get("https://api.exchangerate.host/latest")
	my_json = response.json()
	orig_amount = my_json['rates']
	myForm = converterForm()

	if request.method == 'POST':
		amount = request.POST['amount']
		my_currency = request.POST['my_currency']
		to_currency = request.POST['to_currency']

		if my_currency != 'EUR':
			eur_amount = int(amount) / orig_amount[my_currency]
			converted_amount = eur_amount * orig_amount[to_currency]
		else:
			converted_amount = int(amount) * orig_amount[to_currency]

	return render(request,'converter/home.html',{'myForm':myForm,'converted_amount':converted_amount})