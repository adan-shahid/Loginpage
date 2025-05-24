from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from web.forms import loginForm

# Create your views here.

def home(request):
    return render(request, 'web/index.html')

def loginPage(request):
    form = loginForm()
    
    if request.method == "POST":

        login_form = form(request.POST)
        
        if login_form.is_valid():
            form.save()
            return redirect('web/index.html')
                
            
    context = {'form': form}
    return render(request, 'web/login.html', context)

def signupPage(request):
    return render(request,'web/register.html')
