from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def hello(request):
	form = converterForm
	if request.method == 'POST':
		amount = request.POST['amount']
		my_currency = request.POST['my_currency']
		to_currency = request.POST['to_currency']

		if my_currency != 'EUR':
			amount_in_euro = int(amount) / rates.get(my_currency)
			new_amount = amount_in_euro * rates.get(to_currency)

		elif str(my_currency) == 'EUR':
			new_amount = int(amount) * rates.get(to_currency)

		my_currency_symbol = CurrencySymbols.get_symbol(my_currency)
		to_currency_symbol = CurrencySymbols.get_symbol(to_currency)

		my_dict = {
			'new_amount': new_amount,
			'amount': amount,
			'my_currency_symbol': my_currency_symbol,
			'to_currency_symbol': to_currency_symbol,
		}

		return render(request, 'converter/ans.html', my_dict)

	else:
	    return render(request, 'converter/home.html', {'form':form})