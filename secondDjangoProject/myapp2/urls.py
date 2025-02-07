from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'),
    path('foods/<str:category>/', views.list_Of_Food, name='list_of_food'),
    path('register/', views.register, name='register'),

]

