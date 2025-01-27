from django.shortcuts import render
from django.http import HttpResponse

# create your view here
def home(request):
    content = "<html><body><h1>Welcome my People no one hack my account na me yan wetin I yan:</h1></body></html>"
    return HttpResponse(content)




