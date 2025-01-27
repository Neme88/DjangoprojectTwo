from django.shortcuts import render
from django.http import HttpResponse

# create your view here
def home(request):
    content = "<html><body><h1>Welcome my people na me yan wetin I yan</h1></body></html>"
    return HttpResponse(content)



