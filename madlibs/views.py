# madlibs/views.py
import sys
import datetime
from importlib import reload
from django.shortcuts import render
from .models import MadLib
from django import forms
import logging
import inspect
from . import StoredMadlibs

logging.basicConfig(filename="madlib_errors.log", level=logging.ERROR)

#  Creates the form we need to dynamically
# As we add user inputted stories, we need to be able to handle those
class MadlibForm(forms.Form):
    def __init__(self, blanks, *args, **kwargs):
        super(MadlibForm, self).__init__(*args, **kwargs)
        for key in blanks:
            self.fields[key] = forms.CharField(label=blanks[key])

def madlib_list(request):
    # Fetch the list of MadLib classes
    classes = [
        name
        for name in dir(StoredMadlibs)
        if inspect.isclass(getattr(StoredMadlibs, name, None))
    ]

    # Render the template with the list of MadLib classes
    return render(request, "madlib_list.html", {"classes": classes})

# Is not needed right for now since I am not looking for stored madlibs at this point
# def madlib_detail(request, madlib_id):
#     madlib = MadLib.objects.get(id=madlib_id)
#     return render(request, "madlib_detail.html", {"madlib": madlib})

# Just simple call to hello world and takes in the date format. 
def hello_view(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})

#  handles the call to the home or base page 
def home(request):
    return render(request, "base.html")

# This handles the meat and potatoes of the program
def madlib(request, madlib_class):
    error = {}
    try:
        # Grabs our madlib class
        klass = getattr(StoredMadlibs, madlib_class)
        m = klass()
        blanks = m.blanks()
        story = ""
        # Checks if submit request is mad
        if request.method == "POST":
            form = MadlibForm(blanks, request.POST)
            # Makes sure everything is correct in the form
            if form.is_valid():
                answers = form.cleaned_data

                try:
                    # Puts in the answers into the saved madlib
                    story = m.story(answers)
                    # Checks for errors
                except KeyError as ke:
                    error = {"type": "KeyError", "message": str(ke)}
                    logging.error(error)
                    # This will call our error page and read the error that occurs
                    return render(request, "madlib-exception.html", {"error": error})


                # print("Generated Story:", story)
                # Return the template with the story and other variables
                return render(
                    request,
                    "madlib_form.html",
                    {"story": story, "madlib_name": madlib_class, "madlib_class": madlib_class, "form": form},
                )

            else:
                logging.error(form.errors)
        else:
            form = MadlibForm(blanks=blanks)

        # Returns back to the original form
        return render(
            request,
            "madlib_form.html",
            {"madlib_class": madlib_class, "form": form},
        )
    except (ImportError, AttributeError, SyntaxError) as e:
        error = {"type": type(e).__name__, "message": str(e)}
        logging.error(error)

    # Return the exception template with the error information
    return render(request, "madlib-exception.html", {"error": error})
