from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# create your view here
def home(request):
    content = "<html><body><h1>Welcome my People no one hack my account na me yan wetin I yan:</h1></body></html>"
    return HttpResponse(content)

def drinks(request:HttpRequest, drink_name:str) -> HttpResponse:
    drink = {
        'mocha': 'Is a type of coffee',
        'tea': 'Is a type of beverage',
        'lemonade': 'Is a type of refreshment'
    }
    choice_of_drink = drink.get(drink_name, "Sorry we do not have that drink")
    return HttpResponse(f"<h2>{drink_name}</h2> {choice_of_drink}" )







