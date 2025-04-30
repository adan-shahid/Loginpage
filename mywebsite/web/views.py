from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from web.forms import Inputform

# Create your views here.

def home(request):
    return render(request, 'web/index.html')

def loginPage(request):
    form = Inputform()
    
    if request.method == "POST":

        form = Inputform(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            
    context = {'form': form}
    return render(request, 'web/login.html', context)

def signupPage(request):
    return render(request,'web/register.html')
