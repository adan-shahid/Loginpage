from django.shortcuts import render, HttpResponse
from web.forms import Inputform

# Create your views here.

def home(request):
    return render(request, 'web/index.html')

def loginPage(request):
    form = Inputform()
    context = {
        'form': form
    }
    return render(request, 'web/login.html', context)

def signupPage(request):
    return render(request,'web/register.html')
