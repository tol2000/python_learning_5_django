# noinspection PyUnresolvedReferences
from python_learning_5_django.settings.base import *

# SECURITY WARNING: Keep the key in secret place!
SECRET_KEY = open('secret')

# SECURITY WARNING: Do not set to true on prod!
DEBUG = False

ALLOWED_HOSTS = ['myhost.com']
