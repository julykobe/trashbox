from django.http import HttpResponse
from django.shortcuts import render_to_response

from django import forms

class myForm(forms.Form):
    subject = forms.CharField()

def hello(request):
    f = myForm({'subject':'good'})
    return render_to_response('base.html', {'form':f})
