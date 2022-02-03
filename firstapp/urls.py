from django.contrib import admin
from django.urls import path
from firstapp import views
import firstapp

app_name = 'firstapp'

urlpatterns = [
    path('',views.index, name='index' ),
    path('book/<int:book_id>/',views.detail, name='detail' ),
]
