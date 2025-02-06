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

def list_Of_Food(request:HttpRequest, category:str) -> HttpResponse:
    food_categories = {
        'vegetarian': ["cereal", "Bean", "Plaintain"],
        'non-vegetarian': ["pork chops", "Chicken", "Beef"],
        'all': ["Paster", "Cereal", "Beans", "Pork chops", "Plaintain", "Chicken", "Beef"]
}
# Get the list of foods for the given category, default to 'all' if category is unknown
    foods = food_categories.get(category, food_categories['all'])
    # Create a list of foods as HTML
    food_list = "<ul>" + "".join(f"<li>{item}</li>" for item in foods) + "</ul>"
    return HttpResponse(f"<h2>Food Category: {category}</h2>{food_list}")










