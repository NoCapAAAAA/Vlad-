from django.contrib import admin
from django.urls import path
from cart.views import Likes, RemoveLike, AddValue, RemoveValue


app_name = 'category'

urlpatterns = [
    path('add/like', Likes.as_view(), name='adds'),
    path('remove/', RemoveLike.as_view(), name='remove'),
    path('add_value/', AddValue.as_view(), name='add'),
    path('remove_value/', RemoveValue.as_view(), name='remove_value'),
    
]