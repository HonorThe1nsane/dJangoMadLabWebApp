# madlibs/views.py
from django.shortcuts import render
from .models import MadLib  # Import your model

def madlib_list(request):
    madlibs = MadLib.objects.all()  # Replace with your logic to fetch Mad Libs
    return render(request, 'data/madlib_list.html', {'madlibs': madlibs})

def madlib_detail(request, madlib_id):
    madlib = MadLib.objects.get(id=madlib_id)  # Replace with your logic to fetch a specific Mad Lib
    return render(request, 'data/madlib_detail.html', {'madlib': madlib})
