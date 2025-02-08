from django.urls import path
from . import views


app_name = 'myapp2'


urlpatterns = [
    path('',views.home, name='home'),
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'),
    path('foods/<str:category>/', views.list_Of_Food, name='list_of_food'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),


]

