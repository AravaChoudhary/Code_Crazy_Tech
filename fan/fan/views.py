from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome Crazy Code Tech: Home page</h1>")

def about(request):
    return HttpResponse("<h1>Welcome to Crazy Code Tech : About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Crazy Code Tech : Contact page</h1>")