DEBUG = True  # only set to true when in development, set to False when live.
TEMPLATE = True

SECRET_KEY = 'ox_dg)yv9u+u^rp3^=jw6!*nkvk==2j3cz5#nm(8zm*d&x9*n6'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "database.sql",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
ROOT_URLCONF = 'madlibs.urls'

INSTALLED_APPS = [
    # other installed apps...
    'madlibs',  # Add your app here
]