from django.urls import path
from todoapp.views import *

urlpatterns = [
    path('login/',loginPage,name="loginPage"),
    path('logout/',logoutPage,name="logoutPage"),
    path('',todo_index),
    path('list/',list_todo,name="list_todo"),
    path('create/',create_todo,name='create_todo'),
    path('edit/<int:id>/',edit_todo,name='edit_todo'),
    path('delete/<int:id>/',delete_todo,name='delete_todo'),
]