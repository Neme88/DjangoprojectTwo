from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Item
from .forms import ItemForm, UserRegisterationForm

# User Registration
def register(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = UserRegisterationForm()
    return render(request, 'templates/myapp2/register.html', {'form':form})

# User Login
def user_login(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Item_list')
        else:
            return render(request, 'templates/myapp/login.html', {'error':'Invalid credentials'})
    return render(request, 'templates/myapp2/login.html')


# create your view here
def home(request:HttpRequest) -> HttpResponse:
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










