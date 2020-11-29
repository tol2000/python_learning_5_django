from python_learning_5_django.settings import base

# SECURITY WARNING: Keep the key in secret place!
base.SECRET_KEY = open('secret')

# SECURITY WARNING: Do not set to true on prod!
base.DEBUG = False

base.ALLOWED_HOSTS = ['myhost.com']
