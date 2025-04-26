from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'main.html')

def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request,'signup.html')
