from datetime import datetime
from random import choice

from django import template

register = template.Library()

jokes = [
    'Hi-hi-hi',
    'Ha-ha-ha',
    'Ho-ho!',
    'La-la-la...',
    'Be-be :)'
]


@register.simple_tag
def joke(index=None):
    if index:
        try:
            return jokes[index]
        except IndexError:
            return jokes[len(jokes)-1]
    else:
        return choice(jokes)


@register.simple_tag
def page_info():
    return f'(C) Tolyan. Today is {datetime.today().strftime("%d.%m.%Y %H:%M:%S")}'
