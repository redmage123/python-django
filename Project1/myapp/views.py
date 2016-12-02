from django.shortcuts import render
from django.http import HttpResponse
import myapp.forms.name_form
from myapp.forms import name_form

from django.views.generic.edit import FormView

# Create your views here.


def hello1(request):
    text ='''<h1>Hello World</h1>'''
    return HttpResponse(text)

def hello2(request):
    return render(request,"hello.html")

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return (HTTPResponseRedirect('/thanks/'))
    else:
        form = myapp.forms.name_form.NameForm()
        print ("form = ", form)

    return render(request,'name.html',{form: form})


