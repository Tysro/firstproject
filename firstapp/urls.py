from django.contrib import admin
from django.urls import path
from firstapp import views
import firstapp

app_name = 'firstapp'  #this is a namespace the variable has special meaning on django with name of the app 
# we can write more specific urls like name of the app plus urls.

urlpatterns = [
    path('',views.index, name='index' ),
    path('book<int:book_id>/',views.detail, name='detail' ),
]
