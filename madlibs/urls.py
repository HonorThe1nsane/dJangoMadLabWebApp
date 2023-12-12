# madlibs/urls.py
from django.urls import path
from .views import madlib_list, madlib_detail, hello_view, home, madlib

urlpatterns = [
    path('', madlib_list, name='madlib_list'),
    path('<str:madlib_class>/', madlib, name='madlib'),
    path('hello/', hello_view, name='hello_view'),
    path('home/', home, name='home'),
    # Add other URLs as needed
]
