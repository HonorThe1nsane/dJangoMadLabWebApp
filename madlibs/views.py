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


def madlib_detail(request, madlib_id):
    madlib = MadLib.objects.get(id=madlib_id)
    return render(request, "madlib_detail.html", {"madlib": madlib})


def hello_view(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})


def home(request):
    return render(request, "base.html")


def madlib(request, madlib_class):
    error = {}
    try:
        klass = getattr(StoredMadlibs, madlib_class)
        m = klass()
        blanks = m.blanks()
        story = ""

        if request.method == "POST":
            form = MadlibForm(blanks, request.POST)

            if form.is_valid():
                answers = form.cleaned_data

                try:
                    story = m.story(answers)
                except KeyError as ke:
                    error = {"type": "KeyError", "message": str(ke)}
                    logging.error(error)
                    return render(request, "madlib-exception.html", {"error": error})

                return render(
                    request,
                    "madlib.html",
                    {"story": story, "madlib_name": madlib_class, "form": form},
                )
            else:
                logging.error(form.errors)

        else:
            form = MadlibForm(blanks=blanks)

        return render(
            request,
            "madlib_form.html",  # Render the form template
            {"madlib_name": madlib_class, "form": form},
        )

    except (ImportError, AttributeError, SyntaxError) as e:
        error = {"type": type(e).__name__, "message": str(e)}
        logging.error(error)

    return render(request, "madlib-exception.html", {"error": error})
