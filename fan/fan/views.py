from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return HttpResponse("<h1>Welcome to Crazy Code Tech : About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Crazy Code Tech : Contact page</h1>")