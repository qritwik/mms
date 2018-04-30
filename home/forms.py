from django import forms

class HomeForm(forms.Form):
	Excelsheet = forms.FileField()
	

