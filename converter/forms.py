from django import forms
import requests

response = requests.get("https://api.exchangerate.host/latest")
currency = response.json()

CURRENCY_CHOICE = []

for x in currency['rates']:
	CURRENCY_CHOICE.append((x,x))

class converterForm(forms.Form):
	amount = forms.IntegerField()
	my_currency = forms.ChoiceField(choices=CURRENCY_CHOICE)
	to_currency = forms.ChoiceField(choices=CURRENCY_CHOICE)