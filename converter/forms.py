from django import forms
from .functions import rate_display, symbols_display, convertion_list

rates = rate_display("https://api.exchangerate.host/latest")
symbols = symbols_display(rates)
new_list = convertion_list(symbols)

class converterForm(forms.Form):
	amount = forms.IntegerForm()
	my_currency = forms.ChoiceFiled(choices=new_list)
	to_currency = forms.ChoiceFiled(choices=new_list)