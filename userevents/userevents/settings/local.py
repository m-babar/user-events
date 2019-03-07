from .base import *

DEBUG = True

ALLOWED_HOSTS += [
    '127.0.0.1',
    'localhost',
    ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
