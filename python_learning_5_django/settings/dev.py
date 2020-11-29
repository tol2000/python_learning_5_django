# noinspection PyUnresolvedReferences
from python_learning_5_django.settings.base import *

# SECURITY WARNING: Do not set to true on prod!
DEBUG = False

# For local testing wi will use the local settings
try:
    # noinspection PyUnresolvedReferences
    from python_learning_5_django.settings.local import *
except ImportError:
    pass
