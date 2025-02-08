from django.urls import path
from . import views


app_name = 'myapp2'


urlpatterns = [
    path('home/',views.home, name='home'),
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'),
    path('foods/<str:category>/', views.list_Of_Food, name='list_of_food'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/',views.user_logout, name="logout" ),
    path('', views.item_list, name='item_list'),
    path('item/new/', views.item_create, name='item_create'),


]

