# Overview
This is a MadLib app that I wrote with dJango.
To get started you will need to run the command "python manage.py runserver"
Then go to http://127.0.0.1:8000/home to be able to access the web application
I wrote this to practice using Python and dJango and create a web application.

[Software Demo Video](https://youtu.be/xwKD18bITu4)
[GitHub](https://github.com/HonorThe1nsane/dJangoMadLabWebApp.git)

# Web Pages

You have one main page which is the base.html this is homebase if you want to think of it that way. Then when  you click on the first link it goes to the hello page and that was just a
simple example of Hello World implementation I always try to do first to understand the basics. The you have the madlib_form and that allows you to fill out a madlib. For now it is only
taking from the one madlib that is stored. Eventually I want to be able to institute a database that stores the madlibs and allows others to play them. You have the madlib_list which actually is accessed before the form. It is calling all the madlibs that are stored. Then you have the madlib-exception page which just shows you an error message if there is one.

# Development Environment

Tools used:
VScode
Python
dJango library


# Useful Websites

* [dJango](https://docs.djangoproject.com/en/4.1/howto/static-files/)
* [GitHub Example](https://github.com/deviantintegral/gr8-designs-madlibs.git)
* [Tutorials Point](https://www.tutorialspoint.com/django/django_environment.html)
* [CSS Issues Help](https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django)

# Future Work

* Integrate the stylesheet into a seperate file
* Be able to have different users login
* Users will be able to store their own stories
* Sharing on social media platforms
