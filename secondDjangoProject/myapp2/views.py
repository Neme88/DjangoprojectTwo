from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Item
from .forms import ItemForm, UserRegistrationForm

# User Registration view function feature
def register(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp2/register.html', {'form':form})

# User Login view function feature
def user_login(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp2:item_list')
        else:
            return render(request, 'myapp/login.html', {'error':'Invalid credentials'})
    return render(request, 'myapp2/login.html')

# User Logout view function feature
@login_required
def user_logout(request:HttpRequest) -> HttpResponseRedirect:
    logout(request)
    return redirect('login')

# List all items view function feature (authenticated users only)
@login_required
def item_list(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'myapp2/item_list.html', {'items': items})
# Create a new item view function feature
@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form .is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('myapp2:item_list')
    else:
        form = ItemForm()
    # This below item_form.html file we are returning is yet to be implemented.
    return render(request, 'myapp2/item_form.html', {'form': form})

# Create Update of existing item view function feature
@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('myapp2:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'myapp2/item_form.html', {'form': form})

# view function to create to feature to Delete an Item
@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('myapp2:item_list')
    return render(request, 'myapp2/item_confirm_delete.html', {'item': item})




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










