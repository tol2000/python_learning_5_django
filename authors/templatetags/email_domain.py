from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def cut_email_domain(value):
    if '@' in value:
        return value.partition('@')[2]
    else:
        return ''
