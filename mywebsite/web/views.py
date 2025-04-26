from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'navbar.html')

def loginPage(request):
    return render(request, 'login.html')
