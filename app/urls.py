from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detail/<int:id>/',views.detail,name='detail'),  # since we passed id also from _card.html to display each card separately. so we need to catch the unique id of each contact record.. <> can be used to catch the ID using <int:id> 
    path('search',views.search,name='search'),
    
    
]
